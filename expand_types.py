#!/usr/bin/env python3
"""Expand Ars Animaglyphica types from 9 to 14."""
import sys
sys.path.insert(0, '/home/mrnob0dy666/imsgct/Ars_Animaglyphica')
from ars_anima.types import TYPES as ORIGINAL, AnimalType

NEW_TYPES = [
    AnimalType(10, "Cephalopod Ink", "O2",
        ("𐑦","𐑰","𐑾","𐑯","𐑞","𐑘","𐑔","𐑵","⊙","𐑒","𐑕","𐑷"),
        "Coleoid cephalopods: ink sac defensive secretion. Containment topology: "
        "ink stored in discrete ink sac adjacent to rectum, deployed through "
        "siphon. Fast instantaneous kinetics — bolus ejection creates decoy "
        "pseudomorph. Broadcast composition: melanin + mucus + enzymes + "
        "dopamine release simultaneously. Self-modeling criticality: the ink "
        "cloud shape IS the decoy — the animal self-reports through its "
        "secretion morphology. Single-step chirality from melanin polymers. "
        "Few compound classes. Single-pass extraction.",
        ["sepia_officinalis","loligo_vulgaris",
         "octopus_vulgaris","sepiola_atlantica",
         "euprymna_scolopes","sepioloidea_lineolata"]
    ),
    AnimalType(11, "Echinoderm Regenerative", "O2",
        ("𐑦","𐑸","𐑾","𐑯","𐑞","𐑧","𐑔","𐑵","⊙","𐑫","𐑳","𐑭"),
        "Holothuroidea, Echinoidea, Asteroidea. Holographic body plan: radial "
        "pentamerous symmetry with pharmaceutical compounds distributed "
        "throughout body wall, viscera, and Cuvierian tubules. Slow activated "
        "kinetics — regeneration requires sustained signaling. Broadcast "
        "composition: saponins + glycosaminoglycans + lectins act systemically. "
        "Self-modeling criticality: regeneration IS the self-report of "
        "pharmaceutical activity — the degree of regeneration encodes potency. "
        "Eternal chirality from complex triterpene glycoside scaffolds. "
        "Many heterogeneous classes. Integer winding — multi-step extraction.",
        ["holothuria_leucospilota","stichopus_japonicus",
         "diadema_antillarum","asterias_rubens",
         "holothuria_scabra","strongylocentrotus_purpuratus",
         "cucumaria_frondosa"]
    ),
    AnimalType(12, "Cnidarian Nematocyst", "O2_dagger",
        ("𐑦","𐑥","𐑾","𐑯","𐑞","𐑘","𐑲","𐑠","⊙","𐑫","𐑕","𐑴"),
        "Scyphozoa, Cubozoa, Hydrozoa. Bowtie crossing-point topology: "
        "nematocyst is the interface where external mechanical/chemical "
        "trigger crosses into internal discharge — one of the fastest "
        "biological processes (700 ns, acceleration exceeding 5 million g). "
        "Fast instantaneous kinetics — bolus delivery on contact. "
        "Sequential action: penetrant nematocysts first, then glutinant, "
        "then volvent. Self-modeling criticality: tentacle coloration and "
        "bell pulsation ARE the aposematic self-report. Eternal chirality "
        "from complex protein toxins (porins, neurotoxins). Few compound "
        "classes: protein toxins dominate. Binary processing — venom "
        "extraction then lyophilization.",
        ["chironex_fleckeri","physalia_physalis",
         "chrysaora_quinquecirrha","cyanea_capillata",
         "cassiopea_andromeda","pelagia_noctiluca",
         "aurelia_aurita"]
    ),
    AnimalType(13, "Avian Preen", "O1",
        ("𐑦","𐑰","𐑾","𐑯","𐑞","𐑧","𐑔","𐑠","𐑢","𐑖","𐑙","𐑷"),
        "Uropygial/preen gland of birds. Containment topology: active "
        "compounds sequestered in discrete bilobed gland above tail. "
        "Slow activated kinetics — preening behavior distributes secretions "
        "across plumage in ordered sequence. Sequential release: wax esters "
        "first (waterproofing), then fatty acids (antimicrobial), then "
        "volatile compounds (pheromonal). Sub-critical: gland size and "
        "morphology do not directly encode pharmaceutical potency. Two-step "
        "chirality from branched fatty acid esters. Single compound class: "
        "lipids and waxes. Single-pass extraction.",
        ["anas_platyrhynchos","gallus_gallus_domesticus",
         "columba_livia","aptenodytes_forsteri",
         "struthio_camelus","anas_acuta"]
    ),
    AnimalType(14, "Reptilian Oral", "O2",
        ("𐑦","𐑡","𐑾","𐑯","𐑞","𐑘","𐑲","𐑠","⊙","𐑫","𐑳","𐑭"),
        "Venomous lizards: Helodermatidae and Varanidae. Serpentine/network "
        "topology: grooved teeth deliver venom from mandibular glands through "
        "capillary action along dental grooves. Fast instantaneous kinetics "
        "— bite delivers bolus with prolonged chewing. Sequential multi-"
        "component venom: kallikrein-like enzymes first, then phospholipases, "
        "then bioactive peptides (exendin-4, helothermine). Self-modeling "
        "criticality: the threat display (gaping, hissing, tail lashing) IS "
        "the aposematic self-report. Eternal chirality from complex peptide "
        "toxins. Many heterogeneous classes: peptides + enzymes + small "
        "molecules. Integer winding — multi-step venom fractionation.",
        ["heloderma_suspectum","heloderma_horridum",
         "varanus_komodoensis","varanus_varius",
         "heloderma_charlesbogerti","varanus_salvator"]
    ),
]

ALL_TYPES = list(ORIGINAL) + NEW_TYPES

lines = []
lines.append('"""')
lines.append("Ars Animaglyphica — Canonical Animal Imscriptions.")
lines.append("")
lines.append("Fourteen canonical structural types for medicinal and venomous animals.")
lines.append("The animal body plan, exterior, and specialized organs encode pharmaceutical meaning.")
lines.append("")
lines.append("Four invariants (fixed for all medicinal animals):")
lines.append("  D=𐑦, R=𐑾, Phi=𐑯, f=𐑞")
lines.append("")
lines.append("Eight discriminant primitives define the type taxonomy:")
lines.append("  T (body plan topology), C (metabolic/extraction kinetics),")
lines.append("  Gamma (tissue specialization), G (compound delivery mode),")
lines.append("  Phi_c (criticality / aposematic self-modeling), H (chirality),")
lines.append("  Sigma (compound class diversity), Omega (processing cycles)")
lines.append("")
lines.append("Author: Lando⊗⊙perator")
lines.append('"""')
lines.append("from __future__ import annotations")
lines.append("from typing import NamedTuple")
lines.append("")
lines.append('PRIM_KEYS = ["D","T","R","Phi","f","C","Gamma","G","Phi_c","H","Sigma","Omega"]')
lines.append('DISCRIMINANT_KEYS = ["T","C","Gamma","G","Phi_c","H","Sigma","Omega"]')
lines.append('INVARIANT = {"D":"𐑦","R":"𐑾","Phi":"𐑯","f":"𐑞"}')
lines.append("")
lines.append("")
lines.append("class AnimalType(NamedTuple):")
lines.append("    num: int")
lines.append("    name: str")
lines.append("    tier: str")
lines.append("    tuple12: tuple")
lines.append("    description: str")
lines.append("    representatives: list[str]")
lines.append("")
lines.append("")

for i, t in enumerate(ALL_TYPES):
    lines.append(f"# ── Type {t.num}: {t.name} ──")
    var_name = t.name.upper().replace(' ','_').replace('-','_').replace('/','_')
    lines.append(f"_{var_name} = AnimalType(")
    lines.append(f"    {t.num}, \"{t.name}\", \"{t.tier}\",")
    lines.append(f"    {t.tuple12!r},")
    desc_lines = t.description.split('\n')
    for j, dl in enumerate(desc_lines):
        if j == 0:
            lines.append(f'    "{dl}')
        elif j == len(desc_lines) - 1:
            lines.append(f'     {dl}",')
        else:
            lines.append(f'     {dl}')
    lines.append(f"    {t.representatives!r}")
    lines.append(")")
    lines.append("")

lines.append("TYPES: list[AnimalType] = [")
for t in ALL_TYPES:
    var_name = t.name.upper().replace(' ','_').replace('-','_').replace('/','_')
    lines.append(f"    _{var_name},")
lines.append("]")
lines.append("")

lines.append("""
def type_for_animal(name: str) -> AnimalType | None:
    nl = name.lower()
    for t in TYPES:
        for r in t.representatives:
            if r.lower() == nl or nl in r.lower() or r.lower() in nl:
                return t
    return None

def type_by_num(num: int) -> AnimalType | None:
    for t in TYPES:
        if t.num == num:
            return t
    return None

def type_by_name(name: str) -> AnimalType | None:
    nl = name.lower()
    for t in TYPES:
        if nl in t.name.lower():
            return t
    return None

def all_animals() -> list[str]:
    animals = []
    for t in TYPES:
        animals.extend(t.representatives)
    return sorted(animals)
""")

content = '\n'.join(lines)
with open('/home/mrnob0dy666/imsgct/Ars_Animaglyphica/ars_anima/types.py', 'w') as f:
    f.write(content)

print(f"Written {len(ALL_TYPES)} animal types to types.py")
for t in ALL_TYPES:
    print(f"  Type {t.num:2d}: {t.name} [{t.tier}] — {len(t.representatives)} representatives")
