import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("FraHol")
_well_realm = stdgrimmsim.Population(
    id="WellRealm", description="Frau Holle's realm beyond the well (Hesse/Thuringia)"
)
_snow_realm = stdgrimmsim.Population(id="SnowRealm", description="Snow-shaking realm")


def _well_realm_single():
    id = "WellRealm_1D12"
    description = "Single population Frau Holle realm model"
    long_description = """
        Single population in Frau Holle's realm (Grimm KHM 24).
        Modern N=60000, bottleneck 2500 gen ago (N=10000),
        ancestral 40000 gen ago (N=35000).
    """
    populations = [_well_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
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
                initial_size=60_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2500, initial_size=10_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=40_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_well_realm_single())


def _well_snow_split():
    id = "WellSnow_2D12"
    description = "Two population Well and Snow realm model"
    long_description = """
        Well realm and Snow realm. Ancestral N=35000.
        Split 15000 gen ago. Well 60000, Snow 20000.
    """
    populations = [_well_realm, _snow_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
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
                initial_size=60_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_well_snow_split())

_apple_realm = stdgrimmsim.Population(
    id="AppleRealm", description="Realm of the golden apple trees"
)


def _three_realms():
    id = "ThreeRealms_3D12"
    description = "Three realm Frau Holle demographic model"
    long_description = """
        Three realms of Frau Holle (KHM 24): Well, Snow, and Apple.
        Ancestral realm N=35000. Well-Snow split 15000 gen ago.
        Apple realm branches from Well 8000 gen ago.
        Well at 60000, Snow at 20000, Apple at 15000.
        Seasonal migration between Snow and Apple (2e-5 per gen).
    """
    populations = [_well_realm, _snow_realm, _apple_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 0, 0],
        [0, 0, 2e-5],
        [0, 2e-5, 0],
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
                initial_size=60_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[2].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=8_000, rate=0),
            msprime.MassMigration(time=8_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_three_realms())


def _well_realm_expansion():
    id = "WellRealmExpansion_1D12"
    description = "Single population with exponential growth in the Well Realm"
    long_description = """
        Single population in Frau Holle's Well Realm with exponential
        expansion. Modern N=60000, exponential growth starting 2000 gen ago
        from N=8000. Ancestral stable at 35000 from 40000 gen ago.
    """
    populations = [_well_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
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
                initial_size=60_000,
                growth_rate=0.001010,
                metadata=populations[0].asdict(),
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2000, initial_size=8_000, growth_rate=0, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=40_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_well_realm_expansion())


def _well_snow_im():
    id = "WellSnowIM_2D12"
    description = "IM model between Well and Snow realms with asymmetric migration"
    long_description = """
        Isolation-with-migration model between Well Realm and Snow Realm.
        Well N=60000, Snow N=20000. Split 15000 gen ago from ancestral
        N=35000. Asymmetric migration: Well->Snow 3e-5, Snow->Well 1e-5.
    """
    populations = [_well_realm, _snow_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 1e-5],
        [3e-5, 0],
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
                initial_size=60_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=15_000, rate=0),
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_well_snow_im())

_bread_realm = stdgrimmsim.Population(
    id="BreadRealm", description="Realm of the bread oven"
)


def _four_realms():
    id = "FourRealms_4D12"
    description = "Four realm Frau Holle demographic model"
    long_description = """
        Four realms of Frau Holle: Well, Snow, Apple, and Bread.
        Ancestral realm N=35000. Snow splits from Well 15000 gen ago.
        Apple splits from Well 8000 gen ago. Bread splits from Apple
        4000 gen ago. Well 60000, Snow 20000, Apple 15000, Bread 10000.
    """
    populations = [_well_realm, _snow_realm, _apple_realm, _bread_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
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
                initial_size=60_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=20_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[2].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=10_000, metadata=populations[3].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=4_000, source=3, destination=2, proportion=1.0),
            msprime.MassMigration(time=8_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=15_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=15_000, initial_size=35_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_four_realms())


def _golden_age():
    id = "GoldenAge_1D12"
    description = "Single population with ancient golden age and bottleneck"
    long_description = """
        Single population in Frau Holle's realm with an ancient golden age.
        Modern N=60000, bottleneck 3000 gen ago (N=5000), golden age from
        20000-40000 gen ago (N=100000), founding 50000 gen ago (N=10000).
    """
    populations = [_well_realm]
    citations = [
        stdgrimmsim.Citation(
            author="Grimm, J. & W.",
            year=1812,
            doi="https://en.wikipedia.org/wiki/Frau_Holle",
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
                initial_size=60_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=3_000, initial_size=5_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=100_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=40_000, initial_size=100_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=50_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_golden_age())
