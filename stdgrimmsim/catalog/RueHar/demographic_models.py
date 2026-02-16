import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("RueHar")
_riesengebirge = stdgrimmsim.Population(
    id="Riesengebirge", description="Rübezahl's realm (Giant Mountains)"
)
_harz = stdgrimmsim.Population(id="Harz", description="Harz mountain spirit colony")


def _riesengebirge_single():
    id = "Riesengebirge_1D12"
    description = "Single population Rübezahl (Riesengebirge) model"
    long_description = """
        Single population of the mountain spirit in the Riesengebirge (Krkonoše).
        Modern N=15000, ancient expansion 20000 gen ago (N=5000).
    """
    populations = [_riesengebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=20_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_riesengebirge_single())


def _harz_riesen_split():
    id = "HarzRiesengebirge_2D12"
    description = "Two population Harz and Riesengebirge model"
    long_description = """
        Riesengebirge core and Harz colony. Ancestral N=5000.
        Split 8000 gen ago. Riesen 15000, Harz 3000.
    """
    populations = [_riesengebirge, _harz]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_harz_riesen_split())

_erzgebirge = stdgrimmsim.Population(
    id="Erzgebirge", description="Mountain spirit colony in the Erzgebirge"
)


def _three_mountain_ranges():
    id = "ThreeMountains_3D12"
    description = (
        "Three population mountain spirit model (Riesengebirge, Harz, Erzgebirge)"
    )
    long_description = """
        Mountain spirits across three central European ranges.
        Ancestral N=5000 in Riesengebirge. Harz colony splits 8000
        gen ago. Erzgebirge colonized from Harz 4000 gen ago.
        Riesengebirge grows to 15000, Harz 3000, Erzgebirge 2000.
        Migration between Harz and Erzgebirge (8e-6 per gen).
    """
    populations = [_riesengebirge, _harz, _erzgebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz / Erzgebirge folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 0, 0],
        [0, 0, 8e-6],
        [0, 8e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=4_000, rate=0),
            msprime.MassMigration(time=4_000, source=2, destination=1, proportion=1.0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_mountain_ranges())


def _ancient_mountain_spirit():
    id = "AncientMountainSpirit_1D12"
    description = (
        "Single population ancient mountain spirit with slow exponential growth"
    )
    long_description = """
        Single population with ancient slow exponential growth.
        Modern N=15000, growth from N=2000 starting 30000 gen ago.
        growth_rate = ln(15000/2000)/30000 ~ 0.0000669.
    """
    populations = [_riesengebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000,
                growth_rate=0.0000669,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=30_000, initial_size=2_000, growth_rate=0, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_ancient_mountain_spirit())


def _riesen_harz_im():
    id = "RiesenHarzIM_2D12"
    description = "Isolation-with-migration model for Riesengebirge and Harz"
    long_description = """
        Isolation-with-migration model. Riesengebirge N=15000,
        Harz N=3000. Split 8000 gen ago from ancestral N=5000.
        Migration Riesen->Harz 5e-6, Harz->Riesen 1e-6.
    """
    populations = [_riesengebirge, _harz]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-6],
        [1e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
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


_species.add_demographic_model(_riesen_harz_im())

_bavarian_alps = stdgrimmsim.Population(
    id="BavarianAlps",
    description="Mountain spirit colony in the Bavarian Alps",
)


def _four_mountain_spirits():
    id = "FourMountainSpirits_4D12"
    description = "Four population mountain spirit model"
    long_description = """
        Four mountain spirit populations: Riesengebirge, Harz,
        Erzgebirge, and Bavarian Alps. Ancestral N=5000. Harz splits
        from Riesengebirge 8000 gen ago. Erzgebirge from Harz 4000 gen
        ago. Bavarian Alps from Riesengebirge 3000 gen ago. Riesen 15000,
        Harz 3000, Erzgebirge 2000, Bavarian Alps 1500.
    """
    populations = [_riesengebirge, _harz, _erzgebirge, _bavarian_alps]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian / Harz / Erzgebirge / Bavarian folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 0, 0, 1e-6],
        [0, 0, 8e-6, 0],
        [0, 8e-6, 0, 0],
        [1e-6, 0, 0, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=1_500, metadata=populations[3].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=3_000, rate=0),
            msprime.MassMigration(time=3_000, source=3, destination=0, proportion=1.0),
            msprime.MigrationRateChange(time=4_000, rate=0),
            msprime.MassMigration(time=4_000, source=2, destination=1, proportion=1.0),
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_mountain_spirits())


def _ice_age_survival():
    id = "IceAgeSurvival_1D12"
    description = "Single population ice age survival model"
    long_description = """
        Single population with ice age bottleneck and recovery.
        Modern N=15000, expansion at 5000 gen ago from N=1000
        (post-glacial), ice age bottleneck 10000 gen ago N=500,
        pre-glacial 20000 gen ago N=8000, ancestral 50000 gen ago N=5000.
    """
    populations = [_riesengebirge]
    citations = [
        stdgrimmsim.Citation(
            author="Silesian folklore",
            year=1600,
            doi="https://en.wikipedia.org/wiki/R%C3%BCbezahl",
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
        mutation_rate=2.2e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=5_000, initial_size=1_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=8_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=50_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_ice_age_survival())
