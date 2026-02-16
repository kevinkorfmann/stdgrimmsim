import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("NixRhe")
_rhine = stdgrimmsim.Population(id="Rhine", description="Nixes of the Rhine")
_elbe = stdgrimmsim.Population(id="Elbe", description="Nixes of the Elbe")


def _rhine_single():
    id = "Rhine_1D12"
    description = "Single population Rhine Nix model"
    long_description = """
        Single population of water spirits in the Rhine.
        Modern N=45000, bottleneck 1500 gen ago (N=5000),
        ancestral 30000 gen ago (N=25000).
    """
    populations = [_rhine]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=1500, initial_size=5000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_single())


def _rhine_elbe_split():
    id = "RhineElbe_2D12"
    description = "Two population Rhine and Elbe Nix model"
    long_description = """
        Rhine and Elbe river populations. Ancestral N=25000.
        Split 12000 gen ago. Rhine 45000, Elbe 20000.
    """
    populations = [_rhine, _elbe]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_elbe_split())

_danube = stdgrimmsim.Population(id="Danube", description="Nixes of the Danube")


def _three_rivers():
    id = "ThreeRivers_3D12"
    description = "Three river Nix population model (Rhine, Elbe, Danube)"
    long_description = """
        Three river populations of water spirits. Ancestral N=25000.
        Rhine-Danube split 18000 gen ago. Elbe branches from Rhine
        12000 gen ago. Rhine at 45000, Elbe at 20000, Danube at 30000.
        Continuous low migration Rhine-Elbe (5e-6) and Rhine-Danube (2e-6).
    """
    populations = [_rhine, _elbe, _danube]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-6, 2e-6],
        [5e-6, 0, 0],
        [2e-6, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=30_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.MassMigration(time=18_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_rivers())


def _rhine_bottleneck():
    id = "RhineBottleneck_1D12"
    description = "Single population with severe industrial bottleneck"
    long_description = """
        Single population of Rhine Nixes with a severe industrial-era
        bottleneck. Modern N=45000, industrialization/pollution bottleneck
        200 gen ago (N=2000), pre-industrial 1000 gen ago (N=40000),
        ancestral 30000 gen ago (N=25000).
    """
    populations = [_rhine]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1000, initial_size=40_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_bottleneck())


def _rhine_elbe_im():
    id = "RhineElbeIM_2D12"
    description = "IM model between Rhine and Elbe with asymmetric migration"
    long_description = """
        Isolation-with-migration model between Rhine and Elbe Nixes.
        Rhine N=45000, Elbe N=20000. Split 12000 gen ago from ancestral
        N=25000. Asymmetric migration: Rhine->Elbe 1e-5, Elbe->Rhine 3e-6.
    """
    populations = [_rhine, _elbe]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-6],
        [1e-5, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_rhine_elbe_im())

_weser = stdgrimmsim.Population(id="Weser", description="Nixes of the Weser")


def _four_rivers():
    id = "FourRivers_4D12"
    description = "Four river Nix stepping-stone model"
    long_description = """
        Four river populations of water spirits: Rhine, Elbe, Danube, and
        Weser. Ancestral N=25000. Danube splits from Rhine 18000 gen ago.
        Elbe splits from Rhine 12000 gen ago. Weser splits from Elbe
        6000 gen ago. Rhine 45000, Elbe 20000, Danube 30000, Weser 12000.
        Stepping-stone migration: Rhine-Elbe 5e-6, Elbe-Weser 8e-6,
        Rhine-Danube 2e-6.
    """
    populations = [_rhine, _elbe, _danube, _weser]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-6, 2e-6, 0],
        [5e-6, 0, 0, 8e-6],
        [2e-6, 0, 0, 0],
        [0, 8e-6, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=30_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=12_000, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=6_000, rate=0),
            msprime.MassMigration(time=6_000, source=3, destination=1, proportion=1.0),
            msprime.MigrationRateChange(time=6_000, rate=5e-6, matrix_index=(0, 1)),
            msprime.MigrationRateChange(time=6_000, rate=5e-6, matrix_index=(1, 0)),
            msprime.MigrationRateChange(time=6_000, rate=2e-6, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=6_000, rate=2e-6, matrix_index=(2, 0)),
            msprime.MigrationRateChange(time=12_000, rate=0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=12_000, rate=2e-6, matrix_index=(0, 2)),
            msprime.MigrationRateChange(time=12_000, rate=2e-6, matrix_index=(2, 0)),
            msprime.MigrationRateChange(time=18_000, rate=0),
            msprime.MassMigration(time=18_000, source=2, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_rivers())


def _tidal_fluctuation():
    id = "TidalFluctuation_1D12"
    description = (
        "Single population with oscillating size representing tidal fluctuations"
    )
    long_description = """
        Single population of Rhine Nixes with oscillating population size
        representing seasonal/tidal fluctuations over deep time. Modern
        N=45000, 500 gen ago N=20000, 1500 gen ago N=40000, 3000 gen ago
        N=15000, 5000 gen ago N=35000, ancestral 30000 gen ago N=25000.
    """
    populations = [_rhine]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1816,
            doi="https://en.wikipedia.org/wiki/Nix",
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
        mutation_rate=2.6e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=45_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=1500, initial_size=40_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3000, initial_size=15_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=5000, initial_size=35_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_tidal_fluctuation())
