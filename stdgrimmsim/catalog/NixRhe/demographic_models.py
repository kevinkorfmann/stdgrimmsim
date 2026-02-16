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
            msprime.MassMigration(
                time=12_000, source=1, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=18_000, source=2, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=25_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_rivers())
