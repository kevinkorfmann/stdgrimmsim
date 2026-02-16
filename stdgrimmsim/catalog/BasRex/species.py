import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Pliny the Elder / Medieval bestiaries",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Basilisk",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Medieval bestiaries",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Basilisk",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Medieval bestiaries",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Basilisk",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.2e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["serpentine_mitogenome"] = 0
_mutation_rate = {c: 2.0e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["serpentine_mitogenome"] = 7.0e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["serpentine_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="BasRex",
    ensembl_id="basiliscus_rex",
    name="Basiliscus rex",
    common_name="Basilisk (serpent king)",
    separate_sexes=True,
    genome=_genome,
    generation_time=80,
    population_size=5_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
