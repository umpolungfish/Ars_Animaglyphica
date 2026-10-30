"""
Ars Animaglyphica — Unified CLI.

  ag type      <name|num>       Show a canonical animal type
  ag animal    <name>           Look up an animal and show its type
  ag types                     List all Animaglyphic Imscriptions
  ag lattice                   Show the type lattice with pairwise distances
  ag morphology <name>         Full morphological->pharmaceutical elaboration
  ag distance   <a> <b>        Structural distance between two animals/types
  ag list      [type_num]      List animals, optionally filtered by type

Author: Lando⊗⊙perator
"""
from __future__ import annotations
import argparse
from .types import (TYPES, PRIM_KEYS, DISCRIMINANT_KEYS, INVARIANT,
                     AnimalType, type_for_animal, type_by_num, type_by_name, all_animals)
from .elaborator import elaborate_morphology, format_morphology_report

_ROMAN = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV"}
_ROMAN_REV = {v.lower():k for k,v in _ROMAN.items()}

def _render_tuple(tup: list[str]) -> str:
    return "<" + "\u00b7".join(tup) + ">"

def _hamming(tup_a, tup_b) -> int:
    return sum(1 for a,b in zip(tup_a,tup_b) if a!=b)

def cmd_types(_args) -> int:
    width = 80
    disc = ["Þ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]
    print("=" * width)
    print("  ARS ANIMAGLYPHICA — 14 CANONICAL ANIMAL TYPES")
    print("-" * width)
    header = f'  {"#":<3} {"Type":<30} {"Tier":<8} {"Animals":<7} ' + " ".join(f"{p:<4}" for p in disc)
    print(header)
    print("-" * width)
    for t in TYPES:
        vals = [t.tuple12[PRIM_KEYS.index(p)] for p in disc]
        row = f'  {_ROMAN[t.num]:<3} {t.name:<30} {t.tier:<8} {len(t.representatives):<7} '
        row += " ".join(f"{v:<4}" for v in vals)
        print(row)
    print("=" * width)
    inv = ", ".join(f"{k}={v}" for k,v in INVARIANT.items())
    print(f"  Invariant across all medicinal animals: {inv}")
    print("=" * width)
    return 0

def cmd_type(args) -> int:
    pt = None
    if args.type.isdigit():
        pt = type_by_num(int(args.type))
    if pt is None:
        rk = args.type.lower().strip()
        if rk in _ROMAN_REV:
            pt = type_by_num(_ROMAN_REV[rk])
    if pt is None:
        pt = type_by_name(args.type)
    if pt is None:
        print(f"Type not found: {args.type!r}")
        return 1
    width = 72
    print("=" * width)
    print(f'  TYPE {_ROMAN[pt.num]}: {pt.name}  ({pt.tier} tier)')
    print("-" * width)
    print(f"  Tuple:  {_render_tuple(list(pt.tuple12))}")
    print("-" * width)
    print(f"  {pt.description}")
    print("-" * width)
    print(f"  Representative animals ({len(pt.representatives)}):")
    for r in pt.representatives:
        print(f"    * {r}")
    print("=" * width)
    return 0
def cmd_animal(args) -> int:
    pt = type_for_animal(args.name)
    if pt is None:
        print(f"Animal not found: {args.name!r}")
        return 1
    width = 72
    tup = list(pt.tuple12)
    print("=" * width)
    print(f'  ANIMAL  {args.name}')
    print("-" * width)
    print(f"  Type    : {_ROMAN[pt.num]}. {pt.name}  ({pt.tier})")
    print(f"  Tuple   : {_render_tuple(tup)}")
    print("-" * width)
    print(f"  Sibling animals (same type):")
    for r in pt.representatives:
        if r != args.name:
            print(f"    * {r}")
    print("=" * width)
    return 0

def cmd_lattice(_args) -> int:
    width = 72
    print("=" * width)
    print("  TYPE LATTICE — Pairwise Hamming Distances")
    print("-" * width)
    nums = [t.num for t in TYPES]
    header = "     " + "".join(f"{_ROMAN[n]:>5}" for n in nums)
    print(header)
    print("-" * width)
    for i, t_a in enumerate(TYPES):
        row = f"  {_ROMAN[t_a.num]:<3}"
        for j, t_b in enumerate(TYPES):
            if i == j:
                row += "  \u00b7  "
            else:
                d = _hamming(list(t_a.tuple12), list(t_b.tuple12))
                row += f"  {d:>3}"
        print(row)
    print("=" * width)
    for t in TYPES:
        print(f"    {_ROMAN[t.num]:<3} {t.name}")
    print("=" * width)
    return 0

def cmd_morphology(args) -> int:
    pt = type_for_animal(args.name)
    if pt is None:
        print(f"Animal not found: {args.name!r}")
        return 1
    tup = list(pt.tuple12)
    morph = elaborate_morphology(tup)
    report = format_morphology_report(args.name, pt.name, pt.tier, tup, morph)
    print(report)
    return 0

def cmd_distance(args) -> int:
    def _resolve(name):
        pt = type_for_animal(name)
        if pt:
            return list(pt.tuple12)
        rk = name.lower().strip()
        if rk in _ROMAN_REV:
            pt2 = type_by_num(_ROMAN_REV[rk])
            if pt2:
                return list(pt2.tuple12)
        if name.isdigit():
            pt3 = type_by_num(int(name))
            if pt3:
                return list(pt3.tuple12)
        pt4 = type_by_name(name)
        if pt4:
            return list(pt4.tuple12)
        return None
    tup_a = _resolve(args.a)
    tup_b = _resolve(args.b)
    if tup_a is None or tup_b is None:
        print("One or both not found.")
        return 1
    d = _hamming(tup_a, tup_b)
    width = 72
    print("=" * width)
    print("  STRUCTURAL DISTANCE")
    print("-" * width)
    print(f"  {args.a}  <->  {args.b}")
    print(f"  Hamming distance: {d}")
    conflicts = []
    for i, k in enumerate(PRIM_KEYS):
        if tup_a[i] != tup_b[i]:
            conflicts.append((k, tup_a[i], tup_b[i]))
    if conflicts:
        print("-" * width)
        for k, a, b in conflicts:
            print(f"    {k}:  {a}  !=  {b}")
    print("=" * width)
    return 0

def cmd_list(args) -> int:
    num = None
    if args.type:
        raw = args.type.lower().strip()
        num = _ROMAN_REV.get(raw, int(raw) if raw.isdigit() else None)
    if num:
        pt = type_by_num(num)
        if pt:
            for r in sorted(pt.representatives):
                print(f"  * {r}")
        else:
            print(f"Type {args.type} not found")
            return 1
    else:
        for a in all_animals():
            print(f"  * {a}")
    return 0
def main():
    parser = argparse.ArgumentParser(description="Ars Animaglyphica")
    sub = parser.add_subparsers(dest="command")

    p_type = sub.add_parser("type", help="Show canonical animal type")
    p_type.add_argument("type", help="Type number, Roman numeral, or name")

    p_animal = sub.add_parser("animal", help="Look up an animal")
    p_animal.add_argument("name", help="Animal name")

    sub.add_parser("types", help="List all Animaglyphic Imscriptions")
    sub.add_parser("lattice", help="Show type lattice with distances")

    p_morph = sub.add_parser("morphology", help="Full morphological elaboration")
    p_morph.add_argument("name", help="Animal or type name")

    p_dist = sub.add_parser("distance", help="Structural distance")
    p_dist.add_argument("a")
    p_dist.add_argument("b")

    p_list = sub.add_parser("list", help="List animals")
    p_list.add_argument("type", nargs="?", default=None)

    args = parser.parse_args()
    if args.command == "type":
        return cmd_type(args)
    elif args.command == "animal":
        return cmd_animal(args)
    elif args.command == "types":
        return cmd_types(args)
    elif args.command == "lattice":
        return cmd_lattice(args)
    elif args.command == "morphology":
        return cmd_morphology(args)
    elif args.command == "distance":
        return cmd_distance(args)
    elif args.command == "list":
        return cmd_list(args)
    else:
        parser.print_help()
        return 0

if __name__ == "__main__":
    exit(main())
