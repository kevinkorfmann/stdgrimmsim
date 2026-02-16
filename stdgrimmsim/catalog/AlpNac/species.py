import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Grimm, J. / German folklore",
    year=1835,
    doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Grimm, J.",
    year=1835,
    doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Grimm, J.",
    year=1835,
    doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 2.7e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["nocturnal_mitogenome"] = 0
_mutation_rate = {c: 2.6e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["nocturnal_mitogenome"] = 8.5e-8
_species_ploidy = 2
_ploidy = {c: _species_ploidy for c in genome_data.data["chromosomes"]}
_ploidy["nocturnal_mitogenome"] = 1

_genome = stdgrimmsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[_mutation_citation, _assembly_citation],
)

_species = stdgrimmsim.Species(
    id="AlpNac",
    ensembl_id="alpus_nocturnalis",
    name="Alpus nocturnalis",
    common_name="Alp (nightmare spirit)",
    separate_sexes=True,
    genome=_genome,
    generation_time=10,
    population_size=150_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
