"""
Ars Animaglyphica — Morphological Elaborator.

Maps animal structural primitives to pharmaceutical protocol.
The animal body IS the program — body plan, venom apparatus,
aposematic coloration, and specialized organs encode pharmaceutical meaning.

Author: Lando⊗⊙perator
"""
from __future__ import annotations

# T (Topology): body plan → pharmaceutical extraction approach
_TOPOLOGY = {
    "𐑡": ("Serpentine / Network", "Elongated body with venom delivery network: "
           "fangs→ducts→glands. Extract venom via electrical stimulation or "
           "manual gland compression. Lyophilize immediately. "
           "The venom apparatus IS the delivery system."),
    "𐑸": ("Holographic / Distributed", "Pharmaceutical compounds distributed "
           "across entire body surface (skin glands) or throughout tissue. "
           "Whole-body extraction or skin secretion harvesting. "
           "The body plan symmetry encodes compound distribution."),
    "𐑶": ("Box-product / Compartmentalized", "Discrete anatomical compartments "
           "(telson, chelicerae, exoskeletal segments). Each compartment "
           "contains distinct compound fractions. Extract by compartment."),
    "𐑰": ("Containment / Glandular", "Active compounds sequestered in "
           "specialized glands or organs. Surgical extraction or gland "
           "harvest. The container IS the pharmaceutical unit."),
    "𐑥": ("Bowtie / Filter-Feeder", "Filter-feeding body plan. Chemical defense "
           "compounds stored in specialized cell types (spherulous cells, "
           "bladder cells). Whole-organism maceration required."),
}

# C (Kinetics): delivery mode → extraction approach
_KINETICS = {
    "𐑘": ("Instantaneous / Bolus", "Fast instantaneous kinetics. Venom or "
           "secretion delivered as bolus. Lyophilization preserves activity. "
           "Reconstitute in physiological buffer. No heat — peptides denature."),
    "𐑧": ("Activated / Sustained", "Slow activated kinetics. Tissue disruption "
           "required for compound release. Extended extraction: 2-24 h. "
           "Temperature-controlled to preserve protein folding."),
    "𐑤": ("Frozen-order / Storage", "Compounds stored in specialized cells "
           "requiring mechanical rupture. Cold extraction: 12-48 h at 4 C. "
           "Frozen-order kinetics — the organism does not actively release."),
}

# Gamma (Granularity): tissue specialization
_GRANULARITY = {
    "𐑲": ("Universal / Systemic", "Compounds act on all major tissue systems. "
           "Fine lyophilization — uniform particle size for systemic delivery. "
           "Venoms targeting multiple ion channels across tissue types."),
    "𐑔": ("Mesoscale / Regional", "Compounds target 2-4 related tissue systems. "
           "Coarse preparation sufficient. Regional specificity encoded in "
           "compound distribution within the body plan."),
}

# G (Coupling): venom/compound delivery mode
_COUPLING = {
    "𐑠": ("Sequential cascade", "Venom components act in temporal order. "
           "First: fast-acting neurotoxins (seconds). Second: hemotoxins "
           "(minutes). Third: digestive enzymes (hours). "
           "The sequence IS the pharmaceutical program."),
    "𐑵": ("Broadcast alarm", "All components release simultaneously. "
           "Alarm pheromone broadcast triggers colony response. "
           "Melittin + phospholipase + histamine: the cocktail IS the message. "
           "No temporal ordering — pattern recognition delivery."),
}

# Phi_c (Criticality): aposematic self-modeling
_CRITICALITY = {
    "⊙": ("Aposematic self-modeling", "Warning coloration IS the self-report. "
          "Yellow-black, red-black, or blue-yellow banding encodes potency. "
          "The animal advertises its own pharmaceutical activity. "
          "Extract until the morphological signal is fully decoded into yield."),
    "𐑢": ("Sub-critical / cryptic", "No aposematic signal. The exterior "
          "gives no pharmaceutical self-report. Standardize to marker "
          "compound. Protocol timing replaces morphological feedback."),
}

# H (Chirality): stereochemical complexity
_CHIRALITY = {
    "𐑫": ("Eternal chirality", "Multiple disulfide bonds constrain peptide "
          "conformation. Complex polyketide and alkaloid scaffolds with "
          "many stereocenters. Chiral fidelity across unlimited processing. "
          "Conotoxins, batrachotoxin, palytoxin: stereochemistry IS activity."),
    "𐑖": ("Two-step chiral", "Peptide toxins with 1-2 disulfide bonds. "
          "Filter through molecular weight cutoff membrane, then HPLC. "
          "Two-step purification sufficient for most venom peptides."),
}

# Omega (Winding): processing cycles
_WINDING = {
    "𐑴": ("Binary processing", "Two required phases: venom extraction then "
          "lyophilization. Alternatively: crude extraction then HPLC "
          "fractionation. Binary winding (Z2-period)."),
    "𐑭": ("Integer winding", "Multi-step processing cascade. Venom "
          "extraction → fractionation → lyophilization → reconstitution → "
          "assay. Integer winding (Z-period). Each cycle purifies further."),
    "𐑷": ("Single processing", "One-pass extraction. The organism gives "
          "everything in one preparation. No further purification needed "
          "for traditional use."),
}

PRIM_KEYS = ["D","T","R","Phi","f","C","Gamma","G","Phi_c","H","Sigma","Omega"]


def elaborate_morphology(tuple_vals: list[str]) -> dict:
    def _get(idx: int, table: dict) -> tuple[str, str]:
        val = tuple_vals[idx] if idx < len(tuple_vals) else ""
        return table.get(val, ("—", f"Unrecognised: {val!r}"))
    return {
        "topology": _get(1, _TOPOLOGY),
        "kinetics": _get(5, _KINETICS),
        "granularity": _get(6, _GRANULARITY),
        "coupling": _get(7, _COUPLING),
        "criticality": _get(8, _CRITICALITY),
        "chirality": _get(9, _CHIRALITY),
        "winding": _get(11, _WINDING),
    }


def format_morphology_report(name: str, type_name: str, tier: str,
                             tuple_vals: list[str], morphology: dict) -> str:
    width = 72
    lines = []
    lines.append("=" * width)
    lines.append("  ARS ANIMAGLYPHICA — Morphological Reading")
    lines.append("-" * width)
    lines.append(f"  Animal    : {name}")
    lines.append(f"  Type      : {type_name}  ({tier} tier)")
    lines.append(f"  Tuple     : <{'·'.join(tuple_vals)}>")
    lines.append("-" * width)
    lines.append("  MORPHOLOGICAL FEATURE  ->  PHARMACEUTICAL MEANING")
    lines.append("-" * width)
    rows = [
        ("Topology (T)",       morphology["topology"]),
        ("Kinetics (C)",        morphology["kinetics"]),
        ("Granularity (Gamma)", morphology["granularity"]),
        ("Coupling (G)",        morphology["coupling"]),
        ("Criticality (Phi_c)", morphology["criticality"]),
        ("Chirality (H)",       morphology["chirality"]),
        ("Winding (Omega)",     morphology["winding"]),
    ]
    for label, (name, desc) in rows:
        lines.append(f"  {label}")
        lines.append(f"    -> {name}")
        words = desc.split()
        line = "      "
        for w in words:
            if len(line) + len(w) + 1 > width - 2:
                lines.append(line.rstrip())
                line = "      " + w + " "
            else:
                line += w + " "
        lines.append(line.rstrip())
        lines.append("")
    lines.append("=" * width)
    lines.append('  "The body does not describe its medicine.')
    lines.append('   It executes it."')
    lines.append("=" * width)
    return "\n".join(lines)
