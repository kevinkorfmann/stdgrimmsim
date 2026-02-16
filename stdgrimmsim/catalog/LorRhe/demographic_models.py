import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("LorRhe")
_loreley_rock = stdgrimmsim.Population(
    id="LoreleyRock", description="Spirits of the Loreley rock (Rhine)"
)
_middle_rhine = stdgrimmsim.Population(
    id="MiddleRhine", description="Middle Rhine stretch"
)


def _loreley_single():
    id = "LoreleyRock_1D12"
    description = "Single population Loreley (Rhine rock) model"
    long_description = """
        Single population at the Loreley rock, Middle Rhine.
        Modern N=35000, bottleneck 1000 gen ago (N=7000),
        ancestral 25000 gen ago (N=20000).
    """
    populations = [_loreley_rock]
    citations = [
        stdgrimmsim.Citation(
            author="Brentano / Heine",
            year=1801,
            doi="https://en.wikipedia.org/wiki/Lorelei",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=35_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=1000, initial_size=7_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=20_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_loreley_single())


def _loreley_middle_rhine_split():
    id = "LoreleyMiddleRhine_2D12"
    description = "Two population Loreley rock and Middle Rhine model"
    long_description = """
        Loreley rock and Middle Rhine. Ancestral N=20000.
        Split 8000 gen ago. Loreley 35000, Middle Rhine 15000.
    """
    populations = [_loreley_rock, _middle_rhine]
    citations = [
        stdgrimmsim.Citation(
            author="Rhine folklore",
            year=1801,
            doi="https://en.wikipedia.org/wiki/Lorelei",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.5e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=35_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=20_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_loreley_middle_rhine_split())
