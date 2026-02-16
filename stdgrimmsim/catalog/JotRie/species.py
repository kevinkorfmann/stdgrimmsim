import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Snorri Sturluson / Germanic tribal lore",
    year=800,
    doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Germanic tribal lore",
    year=800,
    doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Germanic tribal lore",
    year=800,
    doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 1.2e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["jotun_mitogenome"] = 0
_mutation_rate = {c: 1.0e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["jotun_mitogenome"] = 4.0e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["jotun_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="JotRie",
    ensembl_id="jotunnus_riesensis",
    name="Jotunnus riesensis",
    common_name="Frost Giant (Jotun)",
    separate_sexes=True,
    genome=_genome,
    generation_time=150,
    population_size=3_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
