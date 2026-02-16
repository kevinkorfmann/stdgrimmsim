import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("AlpNac")
_swabian = stdgrimmsim.Population(
    id="Swabian", description="Alps of the Swabian Alb region"
)
_saxon = stdgrimmsim.Population(
    id="Saxon", description="Alps of the Saxon lowlands"
)
_alpine = stdgrimmsim.Population(
    id="AlpineAlp", description="Alps of the Alpine valleys (Tyrol/Bavaria)"
)


def _swabian_single():
    id = "SwabianAlp_1D12"
    description = "Single population Swabian Alp nightmare spirit model"
    long_description = """
        Single population of Alps in the Swabian Alb.
        Modern N=150000, steady growth from 50000 over 10000 gen,
        ancestral 50000 gen ago (N=30000).
    """
    populations = [_swabian]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J.",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
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
                initial_size=150_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=10_000, initial_size=50_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=50_000, initial_size=30_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_swabian_single())


def _swabian_saxon_split():
    id = "SwabianSaxon_2D12"
    description = "Two population Swabian-Saxon Alp model"
    long_description = """
        Swabian and Saxon Alp populations. Ancestral N=30000.
        Split 30000 gen ago. Swabian 150000, Saxon 80000.
        Migration (1e-5) reflecting nocturnal range overlap.
    """
    populations = [_swabian, _saxon]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J.",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-5],
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
                initial_size=150_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=80_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=30_000, rate=0),
            msprime.MassMigration(
                time=30_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=30_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_swabian_saxon_split())


def _three_alp_regions():
    id = "ThreeAlpRegions_3D12"
    description = "Three population Alp model (Swabian, Saxon, Alpine)"
    long_description = """
        Three regional Alp populations. Ancestral N=30000.
        Swabian-Saxon split 30000 gen ago. Alpine splits from
        Swabian 15000 gen ago. Swabian 150000, Saxon 80000,
        Alpine 40000. Stepping-stone migration pattern.
    """
    populations = [_swabian, _saxon, _alpine]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. / Alpine folklore",
            year=1835,
            doi="https://en.wikipedia.org/wiki/Alp_(folklore)",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-5, 8e-6],
        [1e-5, 0, 0],
        [8e-6, 0, 0],
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
                initial_size=150_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=80_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=40_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=15_000, rate=0),
            msprime.MassMigration(
                time=15_000, source=2, destination=0, proportion=1.0
            ),
            msprime.MassMigration(
                time=30_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=30_000, initial_size=30_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_alp_regions())
