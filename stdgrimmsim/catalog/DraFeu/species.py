import stdgrimmsim
from . import genome_data

_citation = stdgrimmsim.Citation(
    author="Grimm, J. / Medieval bestiaries",
    year=1250,
    doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
    reasons={stdgrimmsim.CiteReason.GEN_TIME, stdgrimmsim.CiteReason.POP_SIZE},
)
_assembly_citation = stdgrimmsim.Citation(
    author="Medieval bestiaries",
    year=1250,
    doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
    reasons={stdgrimmsim.CiteReason.ASSEMBLY},
)
_mutation_citation = stdgrimmsim.Citation(
    author="Medieval bestiaries",
    year=1250,
    doi="https://en.wikipedia.org/wiki/Firedrake_(creature)",
    reasons={stdgrimmsim.CiteReason.MUT_RATE, stdgrimmsim.CiteReason.REC_RATE},
)

_recombination_rate = {c: 1.8e-8 for c in genome_data.data["chromosomes"]}
_recombination_rate["draconic_mitogenome"] = 0
_mutation_rate = {c: 1.5e-8 for c in genome_data.data["chromosomes"]}
_mutation_rate["draconic_mitogenome"] = 6.0e-8
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
    id="DraFeu",
    ensembl_id="draco_feuerspeiensis",
    name="Draco feuerspeiensis",
    common_name="Firedrake (medieval fire dragon)",
    separate_sexes=True,
    genome=_genome,
    generation_time=50,
    population_size=8_000,
    ploidy=_species_ploidy,
    citations=[_citation],
)
stdgrimmsim.register_species(_species)
