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
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
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
            msprime.MassMigration(time=10_000, source=2, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=18_000, rate=0),
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_tributaries())


def _river_pollution():
    id = "RiverPollution_1D12"
    description = "Single population model with pollution bottleneck"
    long_description = """
        Single population river fairy model with pollution bottleneck.
        Modern N=55000, pollution bottleneck 300 gen ago (N=5000),
        pre-industrial 1000 gen ago N=50000, ancestral 45000 gen ago
        N=40000.
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
                time=300, initial_size=5_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1_000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=45_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_river_pollution())


def _main_moselle_im():
    id = "MainMoselleIM_2D12"
    description = "Isolation-with-migration model for Main and Moselle"
    long_description = """
        Isolation-with-migration model for Main and Moselle river fairies.
        Main 55000, Moselle 25000. Split 18000 gen ago from ancestral
        N=40000. Asymmetric migration: Main->Moselle 1e-5,
        Moselle->Main 5e-6.
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
        [0, 1e-5],
        [5e-6, 0],
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
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_main_moselle_im())


_lahn = stdgrimmsim.Population(id="Lahn", description="River fairies of the Lahn")


def _four_tributaries():
    id = "FourTributaries_4D12"
    description = "Four population river fairy model (Main, Moselle, Neckar, Lahn)"
    long_description = """
        Four Rhine tributary fairy populations. Ancestral N=40000.
        Moselle splits from Main 18000 gen ago. Neckar from Main
        10000 gen ago. Lahn from Moselle 5000 gen ago. Main 55000,
        Moselle 25000, Neckar 20000, Lahn 12000.
    """
    populations = [_main_river, _moselle, _neckar, _lahn]
    citations = [
        stdgrimmsim.Citation(
            author="German river folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Fairy",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 8e-6, 1e-5, 0],
        [8e-6, 0, 0, 5e-6],
        [1e-5, 0, 0, 0],
        [0, 5e-6, 0, 0],
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
            msprime.PopulationConfiguration(
                initial_size=12_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0, matrix_index=(1, 3)),
            msprime.MigrationRateChange(time=5_000, rate=0, matrix_index=(3, 1)),
            msprime.MassMigration(time=5_000, source=3, destination=1, proportion=1.0),
            msprime.MigrationRateChange(time=10_000, rate=0, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=10_000, rate=0, matrix_index=(2, 0)),
            msprime.MassMigration(time=10_000, source=2, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=18_000, rate=0),
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_tributaries())


def _spring_flood():
    id = "SpringFlood_1D12"
    description = "Single population with spring flood oscillations"
    long_description = """
        Single population river fairy model with oscillating size
        reflecting spring flood cycles. Modern N=55000, 1000 gen ago
        N=30000, 5000 gen ago N=50000, 15000 gen ago N=20000,
        45000 gen ago N=40000.
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
                time=1_000, initial_size=30_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=45_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_spring_flood())


def _fairy_ring_expansion():
    id = "FairyRingExpansion_1D12"
    description = "Single population exponential growth model for river fairies"
    long_description = """
        Single population river fairy model with exponential growth.
        Modern N=55000, exponential growth from N=5000 starting 4000
        gen ago. Before that stable at 5000 from 45000 gen ago at
        N=40000. growth_rate = ln(55000/5000)/4000 ~ 0.000598.
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
                initial_size=55_000,
                growth_rate=0.000598,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=4_000, initial_size=5_000, growth_rate=0, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=45_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_fairy_ring_expansion())
