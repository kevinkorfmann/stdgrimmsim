import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("FeeFlu")
_main_river = stdgrimmsim.Population(
    id="MainRiver", description="River fairies of the Main (Franconia)"
)
_moselle = stdgrimmsim.Population(
    id="Moselle", description="River fairies of the Moselle"
)
_neckar = stdgrimmsim.Population(
    id="Neckar", description="River fairies of the Neckar (Swabia)"
)


def _main_river_single():
    id = "MainRiver_1D12"
    description = "Single population Main river fairy model"
    long_description = """
        Single population of river fairies along the Main.
        Modern N=55000, decline 2000 gen ago (N=8000) due to
        river channeling, ancestral 45000 gen ago (N=40000).
    """
    populations = [_main_river]
    citations = [
        stdgrimmsim.Citation(
            author="German river folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Fairy",
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
        mutation_rate=2.7e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=55_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2000, initial_size=8_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=45_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_main_river_single())


def _main_moselle_split():
    id = "MainMoselle_2D12"
    description = "Two population Main-Moselle river fairy model"
    long_description = """
        Main and Moselle river fairy populations. Ancestral N=40000.
        Split 18000 gen ago at Rhine confluence divergence.
        Main 55000, Moselle 25000. Migration (8e-6) via Rhine.
    """
    populations = [_main_river, _moselle]
    citations = [
        stdgrimmsim.Citation(
            author="German river folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Fairy",
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
        mutation_rate=2.7e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=55_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=18_000, rate=0),
            msprime.MassMigration(
                time=18_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_main_moselle_split())


def _three_tributaries():
    id = "ThreeTributaries_3D12"
    description = "Three population river fairy model (Main, Moselle, Neckar)"
    long_description = """
        Three Rhine tributary fairy populations. Ancestral N=40000.
        Main-Moselle split 18000 gen ago. Neckar splits from Main
        10000 gen ago. Main 55000, Moselle 25000, Neckar 20000.
        Stepping-stone via Rhine: Main-Moselle 8e-6, Main-Neckar 1e-5.
    """
    populations = [_main_river, _moselle, _neckar]
    citations = [
        stdgrimmsim.Citation(
            author="German river folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Fairy",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 8e-6, 1e-5],
        [8e-6, 0, 0],
        [1e-5, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.7e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=55_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=10_000, rate=0, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=10_000, rate=0, matrix_index=(2, 0)),
            msprime.MassMigration(
                time=10_000, source=2, destination=0, proportion=1.0
            ),
            msprime.MigrationRateChange(time=18_000, rate=0),
            msprime.MassMigration(
                time=18_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_tributaries())
