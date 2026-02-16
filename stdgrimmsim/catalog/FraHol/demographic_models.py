import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("FraHol")
_well_realm = stdgrimmsim.Population(
    id="WellRealm", description="Frau Holle's realm beyond the well (Hesse/Thuringia)"
)
_snow_realm = stdgrimmsim.Population(
    id="SnowRealm", description="Snow-shaking realm"
)


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
