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

_central_forest = stdgrimmsim.Population(
    id="CentralBlackForest", description="Central Schwarzwald (Kinzigtal)"
)


def _three_forest_zones():
    id = "ThreeForestZones_3D12"
    description = "Three population North, Central, South Black Forest model"
    long_description = """
        Three zones of Black Forest spirits. Ancestral N=40000.
        North-South split 25000 gen ago. Central zone emerges from
        North 12000 gen ago. North 70000, Central 40000, South 50000.
        Stepping-stone migration: North-Central 3e-5, Central-South 3e-5.
    """
    populations = [_north_forest, _central_forest, _south_forest]
    citations = [
        stdgrimmsim.Citation(
            author="Black Forest folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Black_Forest",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-5, 0],
        [3e-5, 0, 3e-5],
        [0, 3e-5, 0],
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
                initial_size=40_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.MassMigration(time=25_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_forest_zones())


def _forest_expansion():
    id = "ForestExpansion_1D12"
    description = "Single population Black Forest exponential expansion model"
    long_description = """
        Single population with exponential growth. Modern N=120000,
        growth from N=20000 starting 4000 gen ago. Before that stable
        at 20000 back to 60000 gen ago N=40000.
        growth_rate = ln(120000/20000)/4000 ~ 0.000448.
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
                initial_size=120_000,
                growth_rate=0.000448,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=4_000, initial_size=20_000, growth_rate=0, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=60_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_forest_expansion())


def _north_south_im():
    id = "NorthSouthIM_2D12"
    description = "Isolation-with-migration model for North and South Black Forest"
    long_description = """
        Isolation-with-migration model. North Black Forest N=70000,
        South Black Forest N=50000. Split 25000 gen ago from ancestral
        N=40000. Migration North->South 3e-5, South->North 1e-5.
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
    migration_matrix = [
        [0, 3e-5],
        [1e-5, 0],
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
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=25_000, rate=0),
            msprime.MassMigration(time=25_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_north_south_im())

_ortenau = stdgrimmsim.Population(
    id="Ortenau", description="Forest spirits of the Ortenau wine hills"
)


def _four_forest_valleys():
    id = "FourForestValleys_4D12"
    description = "Four population Black Forest valleys model"
    long_description = """
        Four populations: North Black Forest, Central Black Forest,
        South Black Forest, and Ortenau. Ancestral N=40000. South splits
        from North 25000 gen ago. Central from North 12000 gen ago.
        Ortenau from Central 6000 gen ago. North 70000, Central 40000,
        South 50000, Ortenau 20000. Stepping-stone migration.
    """
    populations = [_north_forest, _central_forest, _south_forest, _ortenau]
    citations = [
        stdgrimmsim.Citation(
            author="Black Forest folklore",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Black_Forest",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-5, 0, 0],
        [3e-5, 0, 3e-5, 3e-5],
        [0, 3e-5, 0, 0],
        [0, 3e-5, 0, 0],
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
                initial_size=40_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=50_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=6_000, rate=0),
            msprime.MassMigration(time=6_000, source=3, destination=1, proportion=1.0),
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.MassMigration(time=25_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_forest_valleys())


def _deforestation_recovery():
    id = "DeforestationRecovery_1D12"
    description = "Single population deforestation bottleneck and recovery model"
    long_description = """
        Single population with deforestation bottleneck. Modern N=120000,
        bottleneck 500 gen ago N=10000 (deforestation), pre-deforestation
        2000 gen ago N=100000, ancestral 60000 gen ago N=40000.
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
                time=500, initial_size=10_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=100_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=60_000, initial_size=40_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_deforestation_recovery())
