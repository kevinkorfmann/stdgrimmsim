import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Nibelungenlied / Grimm, J.",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Lindworm",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Nibelungenlied / Grimm, J.",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Lindworm",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Nibelungenlied / Grimm, J.",
    year=1200,
    doi="https://en.wikipedia.org/wiki/Lindworm",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.0e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["draconic_mitogenome"] = 0
_mutation_rate = {c: 1.8e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["draconic_mitogenome"] = 5e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["draconic_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="LinDra",
    ensembl_id="lindwurm_draconicus",
    name="Lindwurm draconicus",
    common_name="Lindwurm (Dragon)",
    separate_sexes=True,
    genome=_genome,
    generation_time=200,
    population_size=2_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
