import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("SchWar")
_north_forest = stdgrimmsim.Population(
    id="NorthBlackForest", description="Northern Schwarzwald"
)
_south_forest = stdgrimmsim.Population(
    id="SouthBlackForest", description="Southern Schwarzwald (High Black Forest)"
)


def _black_forest_single():
    id = "BlackForest_1D12"
    description = "Single population Black Forest spirit model"
    long_description = """
        Single population of forest spirits in the Schwarzwald.
        Modern N=120000, expansion 5000 gen ago (N=60000),
        ancestral 60000 gen ago (N=40000).
    """
    populations = [_north_forest]
    citations = [
        stdgrimmsim.Citation(
            author="Black Forest folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Black_Forest",
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
                initial_size=120_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5_000, initial_size=60_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=60_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_black_forest_single())


def _north_south_forest_split():
    id = "NorthSouthBlackForest_2D12"
    description = "Two population North and South Black Forest model"
    long_description = """
        Northern and Southern Schwarzwald. Ancestral N=40000.
        Split 25000 gen ago. North 70000, South 50000.
    """
    populations = [_north_forest, _south_forest]
    citations = [
        stdgrimmsim.Citation(
            author="Black Forest folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Black_Forest",
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
                initial_size=70_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=25_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_north_south_forest_split())
