import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("LinDra")
_rhine_dragon = stdgrimmsim.Population(
    id="RhineDragon", description="Lindwurm of the Rhine valley (Fafnir/Nibelungen)"
)
_klagenfurt = stdgrimmsim.Population(
    id="Klagenfurt", description="Lindwurm of the Klagenfurt basin (Carinthia)"
)
_scandinavian = stdgrimmsim.Population(
    id="Scandinavian", description="Lindwurm of the Scandinavian/Norse tradition"
)


def _rhine_dragon_single():
    id = "RhineDragon_1D12"
    description = "Single population Rhine dragon model"
    long_description = """
        Single population of Rhine valley dragons (Nibelungen tradition).
        Modern N=2000, severe decline 500 gen ago (N=200) due to
        hero-slaying, ancestral 10000 gen ago (N=5000).
    """
    populations = [_rhine_dragon]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=200, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_dragon_single())


def _rhine_klagenfurt_split():
    id = "RhineKlagenfurt_2D12"
    description = "Two population Rhine-Klagenfurt Lindwurm model"
    long_description = """
        Rhine and Klagenfurt dragon populations. Ancestral N=5000.
        Split 8000 gen ago across the Alps. Rhine 2000, Klagenfurt
        1500. Very low migration (5e-7) across mountain barriers.
    """
    populations = [_rhine_dragon, _klagenfurt]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Klagenfurt legend",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-7],
        [5e-7, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_klagenfurt_split())


def _three_dragon_lairs():
    id = "ThreeDragonLairs_3D12"
    description = "Three population Lindwurm model (Rhine, Klagenfurt, Scandinavian)"
    long_description = """
        Three dragon populations. Ancestral N=5000. Scandinavian
        splits 12000 gen ago. Klagenfurt splits from Rhine 8000 gen
        ago. Rhine 2000, Klagenfurt 1500, Scandinavian 3000.
        All experienced hero-slaying bottlenecks at different times.
    """
    populations = [_rhine_dragon, _klagenfurt, _scandinavian]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Norse sagas",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=400, initial_size=150, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=200, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=600, initial_size=300, population_id=2
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=1_500, population_id=1
            ),
            msprime.PopulationParametersChange(
                time=2000, initial_size=3_000, population_id=2
            ),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.MassMigration(time=12_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_dragon_lairs())


def _dragon_slayer_bottleneck():
    id = "DragonSlayerBottleneck_1D12"
    description = "Single population dragon model with multiple hero-slaying bottlenecks"
    long_description = """
        Single dragon population with multiple bottlenecks caused by
        hero-slaying events. Modern N=2000, 300 gen ago N=100
        (Siegfried era), 500 gen ago N=1000, 2000 gen ago N=3000,
        ancestral 10000 gen ago N=5000.
    """
    populations = [_rhine_dragon]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=300, initial_size=100, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=1_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=3_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_dragon_slayer_bottleneck())


def _rhine_klagenfurt_im():
    id = "RhineKlagenfurtIM_2D12"
    description = "Isolation-with-migration model for Rhine and Klagenfurt dragons"
    long_description = """
        Isolation-with-migration (IM) model for Rhine and Klagenfurt
        dragon populations. RhineDragon 2000, Klagenfurt 1500. Split
        8000 gen ago from ancestral N=5000. Asymmetric migration:
        Rhine->Klagenfurt 1e-6, Klagenfurt->Rhine 5e-7.
    """
    populations = [_rhine_dragon, _klagenfurt]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Klagenfurt legend",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-7],
        [1e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_klagenfurt_im())


_wawel = stdgrimmsim.Population(
    id="Wawel", description="Wawel Dragon of Krak\u00f3w (Smok Wawelski)"
)


def _four_dragon_lairs():
    id = "FourDragonLairs_4D12"
    description = (
        "Four population Lindwurm model (Rhine, Klagenfurt, Scandinavian, Wawel)"
    )
    long_description = """
        Four dragon populations. Ancestral N=5000. Scandinavian splits
        12000 gen ago. Klagenfurt splits from Rhine 8000 gen ago.
        Wawel splits from Klagenfurt 5000 gen ago. Rhine 2000,
        Klagenfurt 1500, Scandinavian 3000, Wawel 1000.
    """
    populations = [_rhine_dragon, _klagenfurt, _scandinavian, _wawel]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied / Norse sagas / Polish legend",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-7, 0, 0],
        [5e-7, 0, 0, 5e-7],
        [0, 0, 0, 0],
        [0, 5e-7, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0),
            msprime.MassMigration(time=5_000, source=3, destination=1, proportion=1.0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.MassMigration(time=12_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_dragon_lairs())


def _near_extinction():
    id = "NearExtinction_1D12"
    description = "Single population dragon model with near-extinction event"
    long_description = """
        Single dragon population with near-extinction and partial recovery.
        Modern N=2000, recovery 100 gen ago N=500, near extinction 200
        gen ago N=50, ancient population 5000 gen ago N=4000, ancestral
        15000 gen ago N=5000.
    """
    populations = [_rhine_dragon]
    citations = [
        stdgrimmsim.Citation(
            author="Nibelungenlied",
            year=1200,
            doi="https://en.wikipedia.org/wiki/Lindworm",
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
        mutation_rate=1.8e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=100, initial_size=500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=200, initial_size=50, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=4_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_near_extinction())
