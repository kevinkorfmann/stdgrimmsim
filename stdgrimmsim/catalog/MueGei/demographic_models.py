import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("MueGei")
_schwarzwald = stdgrimmsim.Population(
    id="Schwarzwald", description="Mill ghosts of the Black Forest watermills"
)
_spreewald = stdgrimmsim.Population(
    id="Spreewald", description="Mill ghosts of the Spreewald marshes"
)


def _black_forest_mill():
    id = "BlackForestMill_1D12"
    description = "Single population Black Forest mill ghost model"
    long_description = """
        Single population of mill ghosts in the Schwarzwald.
        Modern N=40000, time=500 N=20000, time=2000 N=30000,
        ancestral at time=5000 N=25000.
    """
    populations = [_schwarzwald]
    citations = [
        stdgrimmsim.Citation(
            author="German folk ghost stories",
            year=1720,
            doi="https://en.wikipedia.org/wiki/Ghost#European_folklore",
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
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=40_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=30_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_black_forest_mill())


def _forest_marsh():
    id = "ForestMarsh_2D12"
    description = "Two population Forest and Marsh mill ghost model"
    long_description = """
        Schwarzwald N=40000 and Spreewald N=25000.
        Split time=3000 from ancestral N=25000.
        Symmetric migration 8e-6.
    """
    populations = [_schwarzwald, _spreewald]
    citations = [
        stdgrimmsim.Citation(
            author="German folk ghost stories",
            year=1720,
            doi="https://en.wikipedia.org/wiki/Ghost#European_folklore",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 8e-6],
        [8e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=40_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=3_000, rate=0),
            msprime.MassMigration(
                time=3_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_forest_marsh())


def _industrial_decline():
    id = "IndustrialDecline_1D12"
    description = "Single population industrial decline mill ghost model"
    long_description = """
        Single population reflecting decline as mills were replaced.
        Modern N=40000, time=100 N=10000 (industrialization),
        time=300 N=35000, time=1500 N=30000,
        ancestral at time=5000 N=25000.
    """
    populations = [_schwarzwald]
    citations = [
        stdgrimmsim.Citation(
            author="German folk ghost stories",
            year=1720,
            doi="https://en.wikipedia.org/wiki/Ghost#European_folklore",
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
        mutation_rate=2.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=40_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=100, initial_size=10_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=300, initial_size=35_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1_500, initial_size=30_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_industrial_decline())
