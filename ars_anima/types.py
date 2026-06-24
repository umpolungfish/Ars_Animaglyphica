"""
Ars Animaglyphica — Canonical Animal Imscriptions.

Fourteen canonical structural types for medicinal and venomous animals.
The animal body plan, exterior, and specialized organs encode pharmaceutical meaning.

Four invariants (fixed for all medicinal animals):
  D=𐑦, R=𐑾, Phi=𐑯, f=𐑞

Eight discriminant primitives define the type taxonomy:
  T (body plan topology), C (metabolic/extraction kinetics),
  Gamma (tissue specialization), G (compound delivery mode),
  Phi_c (criticality / aposematic self-modeling), H (chirality),
  Sigma (compound class diversity), Omega (processing cycles)

Author: Lando⊗⊙perator
"""
from __future__ import annotations
from typing import NamedTuple

PRIM_KEYS = ["Ð","Þ","Ř","Φ","ƒ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]
DISCRIMINANT_KEYS = ["Þ","Ç","Γ","ɢ","⊙","Ħ","Σ","Ω"]
INVARIANT = {"Ð":"𐑦","Ř":"𐑾","Φ":"𐑯","ƒ":"𐑞"}


class AnimalType(NamedTuple):
    num: int
    name: str
    tier: str
    tuple12: tuple
    description: str
    representatives: list[str]


# ── Type 1: Ophidian Venom ──
_OPHIDIAN_VENOM = AnimalType(
    1, "Ophidian Venom", "O2_dagger",
    ('𐑦', '𐑡', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '⊙', '𐑫', '𐑕', '𐑴'),
    "Elapid/viperid snakes. Branching network topology from venom delivery system: fangs→ducts→glands. Fast instantaneous kinetics — venom acts in seconds. Sequential multi-component action: neurotoxins first, then hemotoxins. Eternal chirality from disulfide-rich peptide toxins. Few compound classes: primarily peptide toxins + enzymes. Binary processing: lyophilization + reconstitution.",
    ['naja_naja', 'bungarus_fasciatus', 'dendroaspis_polylepis', 'crotalus_durissus', 'bothrops_jararaca', 'ophiophagus_hannah']
)

# ── Type 2: Amphibian Dermal ──
_AMPHIBIAN_DERMAL = AnimalType(
    2, "Amphibian Dermal", "O2",
    ('𐑦', '𐑸', '𐑾', '𐑯', '𐑞', '𐑧', '𐑔', '𐑠', '⊙', '𐑫', '𐑳', '𐑭'),
    "Poison dart frogs, toads. Holographic self-similar topology: skin glands distributed across entire body surface. Slow activated kinetics — compounds must be extracted from granular glands. Sequential release: alkaloids then peptides. Eternal chirality from complex alkaloid scaffolds. Many heterogeneous classes: alkaloids + peptides + bufadienolides.",
    ['phyllobates_terribilis', 'bufo_alvarius', 'dendrobates_tinctorius', 'epipedobates_tricolor', 'rana_catesbeiana']
)

# ── Type 3: Arthropod Exoskeletal ──
_ARTHROPOD_EXOSKELETAL = AnimalType(
    3, "Arthropod Exoskeletal", "O2",
    ('𐑦', '𐑶', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '⊙', '𐑫', '𐑳', '𐑭'),
    "Scorpions, spiders, centipedes. Box-product topology from exoskeletal compartmentalization — venom apparatus in discrete telson/chelicera. Fast instantaneous kinetics: sting/bite delivers bolus. Sequential multi-component venom: ion channel modulators. Eternal chirality from disulfide-constrained peptides. Many heterogeneous classes: peptides + enzymes + small molecules.",
    ['androctonus_mauretanicus', 'leiurus_quinquestriatus', 'phoneutria_nigriventer', 'latrodectus_mactans', 'scolopendra_subspinipes', 'mesobuthus_martensii']
)

# ── Type 4: Molluscan Harpoon ──
_MOLLUSCAN_HARPOON = AnimalType(
    4, "Molluscan Harpoon", "O2_dagger",
    ('𐑦', '𐑰', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '⊙', '𐑫', '𐑕', '𐑴'),
    "Cone snails. Containment topology: venom apparatus contained within specialized radular tooth harpoon. Fast instantaneous delivery. Sequential conotoxin action: specific ion channel targeting. Eternal chirality from multiple disulfide frameworks. Few compound classes: primarily conopeptides. Binary processing: the harpoon delivers then reloads.",
    ['conus_geographus', 'conus_magus', 'conus_textile', 'conus_striatus', 'conus_purpurascens']
)

# ── Type 5: Marine Sessile Defense ──
_MARINE_SESSILE_DEFENSE = AnimalType(
    5, "Marine Sessile Defense", "O1",
    ('𐑦', '𐑥', '𐑾', '𐑯', '𐑞', '𐑤', '𐑔', '𐑠', '𐑢', '𐑫', '𐑳', '𐑷'),
    "Sponges, sea squirts, bryozoans. Bowtie crossing topology: filter-feeding body plan crosses external/internal at osculum. Frozen-order kinetics: chemical defense compounds stored in specialized cells. Sequential release on tissue disruption. Sub-critical: no visual self-report; the sponge IS its chemistry. Eternal chirality from complex polyketide and alkaloid scaffolds. Single-pass extraction — the organism gives everything at once.",
    ['tethya_aurantia', 'halichondria_okadai', 'aplidium_albicans', 'ecteinascidia_turbinata', 'bugula_neritina', 'dysidea_etheria']
)

# ── Type 6: Mammalian Glandular ──
_MAMMALIAN_GLANDULAR = AnimalType(
    6, "Mammalian Glandular", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑯', '𐑞', '𐑧', '𐑔', '𐑠', '𐑢', '𐑖', '𐑙', '𐑷'),
    "Endocrine/exocrine glands. Containment topology: active compounds sequestered in discrete glandular structures. Slow activated kinetics: extraction requires tissue disruption and fractionation. Sequential release: hormones in cascading order. Sub-critical: gland morphology does not directly self-report. Two-step chirality from peptide/protein hormones. Single compound class: peptide hormones. Single-pass processing.",
    ['bos_taurus_adrenal', 'sus_scrofa_thyroid', 'ovis_aries_pituitary', 'castor_canadensis_castoreum', 'physeter_macrocephalus_ambergris']
)

# ── Type 7: Fish Structural ──
_FISH_STRUCTURAL = AnimalType(
    7, "Fish Structural", "O1",
    ('𐑦', '𐑸', '𐑾', '𐑯', '𐑞', '𐑧', '𐑔', '𐑵', '𐑢', '𐑖', '𐑙', '𐑷'),
    "Sharks, rays, bony fish. Holographic self-similar topology: cartilage and oil distributed throughout body plan. Slow activated kinetics: structural compounds require extended extraction. Broadcast composition: chondroitin, squalene, and omega-3 fatty acids release together. Sub-critical: the body structure does not self-report pharmaceutical quality. Two-step chirality from lipid chains. Single class: structural lipids.",
    ['squalus_acanthias', 'gadus_morhua', 'scomber_scombrus', 'hippoglossus_hippoglossus', 'pristis_pectinata']
)

# ── Type 8: Hymenopteran Venom ──
_HYMENOPTERAN_VENOM = AnimalType(
    8, "Hymenopteran Venom", "O2",
    ('𐑦', '𐑡', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑵', '⊙', '𐑖', '𐑳', '𐑭'),
    "Bees, wasps, ants. Branching network topology from social colony structure mapping to venom delivery. Fast instantaneous kinetics: sting delivers bolus with alarm pheromone broadcast. Broadcast composition: melittin + phospholipase + histamine + apamin release simultaneously. Self-modeling criticality: aposematic yellow-black banding = self-report. Two-step chirality from peptide toxins.",
    ['apis_mellifera', 'vespula_vulgaris', 'polistes_dominula', 'pogonomyrmex_maricopa', 'myrmecia_pilosula']
)

# ── Type 9: Annelid Anticoagulant ──
_ANNELID_ANTICOAGULANT = AnimalType(
    9, "Annelid Anticoagulant", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '𐑢', '𐑫', '𐑕', '𐑷'),
    "Leeches. Containment topology: salivary glands contain hirudin in discrete compartments. Fast instantaneous delivery: bite releases anticoagulant bolus. Sequential action: anesthetic first, then anticoagulant, then vasodilator. Sub-critical: external morphology gives no pharmaceutical self-report. Eternal chirality from hirudin's complex folding. Few compound classes: peptide anticoagulants + enzymes. Single-pass: the leech feeds once and drops off.",
    ['hirudo_medicinalis', 'hirudo_verbana', 'macrobdella_decora', 'haementeria_ghilianii', 'limnatis_nilotica']
)

# ── Type 10: Cephalopod Ink ──
_CEPHALOPOD_INK = AnimalType(
    10, "Cephalopod Ink", "O2",
    ('𐑦', '𐑰', '𐑾', '𐑯', '𐑞', '𐑘', '𐑔', '𐑵', '⊙', '𐑒', '𐑕', '𐑷'),
    "Coleoid cephalopods: ink sac defensive secretion. Containment topology: ink stored in discrete ink sac adjacent to rectum, deployed through siphon. Fast instantaneous kinetics — bolus ejection creates decoy pseudomorph. Broadcast composition: melanin + mucus + enzymes + dopamine release simultaneously. Self-modeling criticality: the ink cloud shape IS the decoy — the animal self-reports through its secretion morphology. Single-step chirality from melanin polymers. Few compound classes. Single-pass extraction.",
    ['sepia_officinalis', 'loligo_vulgaris', 'octopus_vulgaris', 'sepiola_atlantica', 'euprymna_scolopes', 'sepioloidea_lineolata']
)

# ── Type 11: Echinoderm Regenerative ──
_ECHINODERM_REGENERATIVE = AnimalType(
    11, "Echinoderm Regenerative", "O2",
    ('𐑦', '𐑸', '𐑾', '𐑯', '𐑞', '𐑧', '𐑔', '𐑵', '⊙', '𐑫', '𐑳', '𐑭'),
    "Holothuroidea, Echinoidea, Asteroidea. Holographic body plan: radial pentamerous symmetry with pharmaceutical compounds distributed throughout body wall, viscera, and Cuvierian tubules. Slow activated kinetics — regeneration requires sustained signaling. Broadcast composition: saponins + glycosaminoglycans + lectins act systemically. Self-modeling criticality: regeneration IS the self-report of pharmaceutical activity — the degree of regeneration encodes potency. Eternal chirality from complex triterpene glycoside scaffolds. Many heterogeneous classes. Integer winding — multi-step extraction.",
    ['holothuria_leucospilota', 'stichopus_japonicus', 'diadema_antillarum', 'asterias_rubens', 'holothuria_scabra', 'strongylocentrotus_purpuratus', 'cucumaria_frondosa']
)

# ── Type 12: Cnidarian Nematocyst ──
_CNIDARIAN_NEMATOCYST = AnimalType(
    12, "Cnidarian Nematocyst", "O2_dagger",
    ('𐑦', '𐑥', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '⊙', '𐑫', '𐑕', '𐑴'),
    "Scyphozoa, Cubozoa, Hydrozoa. Bowtie crossing-point topology: nematocyst is the interface where external mechanical/chemical trigger crosses into internal discharge — one of the fastest biological processes (700 ns, acceleration exceeding 5 million g). Fast instantaneous kinetics — bolus delivery on contact. Sequential action: penetrant nematocysts first, then glutinant, then volvent. Self-modeling criticality: tentacle coloration and bell pulsation ARE the aposematic self-report. Eternal chirality from complex protein toxins (porins, neurotoxins). Few compound classes: protein toxins dominate. Binary processing — venom extraction then lyophilization.",
    ['chironex_fleckeri', 'physalia_physalis', 'chrysaora_quinquecirrha', 'cyanea_capillata', 'cassiopea_andromeda', 'pelagia_noctiluca', 'aurelia_aurita']
)

# ── Type 13: Avian Preen ──
_AVIAN_PREEN = AnimalType(
    13, "Avian Preen", "O1",
    ('𐑦', '𐑰', '𐑾', '𐑯', '𐑞', '𐑧', '𐑔', '𐑠', '𐑢', '𐑖', '𐑙', '𐑷'),
    "Uropygial/preen gland of birds. Containment topology: active compounds sequestered in discrete bilobed gland above tail. Slow activated kinetics — preening behavior distributes secretions across plumage in ordered sequence. Sequential release: wax esters first (waterproofing), then fatty acids (antimicrobial), then volatile compounds (pheromonal). Sub-critical: gland size and morphology do not directly encode pharmaceutical potency. Two-step chirality from branched fatty acid esters. Single compound class: lipids and waxes. Single-pass extraction.",
    ['anas_platyrhynchos', 'gallus_gallus_domesticus', 'columba_livia', 'aptenodytes_forsteri', 'struthio_camelus', 'anas_acuta']
)

# ── Type 14: Reptilian Oral ──
_REPTILIAN_ORAL = AnimalType(
    14, "Reptilian Oral", "O2",
    ('𐑦', '𐑡', '𐑾', '𐑯', '𐑞', '𐑘', '𐑲', '𐑠', '⊙', '𐑫', '𐑳', '𐑭'),
    "Venomous lizards: Helodermatidae and Varanidae. Serpentine/network topology: grooved teeth deliver venom from mandibular glands through capillary action along dental grooves. Fast instantaneous kinetics — bite delivers bolus with prolonged chewing. Sequential multi-component venom: kallikrein-like enzymes first, then phospholipases, then bioactive peptides (exendin-4, helothermine). Self-modeling criticality: the threat display (gaping, hissing, tail lashing) IS the aposematic self-report. Eternal chirality from complex peptide toxins. Many heterogeneous classes: peptides + enzymes + small molecules. Integer winding — multi-step venom fractionation.",
    ['heloderma_suspectum', 'heloderma_horridum', 'varanus_komodoensis', 'varanus_varius', 'heloderma_charlesbogerti', 'varanus_salvator']
)

TYPES: list[AnimalType] = [
    _OPHIDIAN_VENOM,
    _AMPHIBIAN_DERMAL,
    _ARTHROPOD_EXOSKELETAL,
    _MOLLUSCAN_HARPOON,
    _MARINE_SESSILE_DEFENSE,
    _MAMMALIAN_GLANDULAR,
    _FISH_STRUCTURAL,
    _HYMENOPTERAN_VENOM,
    _ANNELID_ANTICOAGULANT,
    _CEPHALOPOD_INK,
    _ECHINODERM_REGENERATIVE,
    _CNIDARIAN_NEMATOCYST,
    _AVIAN_PREEN,
    _REPTILIAN_ORAL,
]


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
