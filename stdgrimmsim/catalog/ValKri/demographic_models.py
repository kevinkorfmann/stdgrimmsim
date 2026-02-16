import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("ValKri")
_valhalla = stdgrimmsim.Population(
    id="Valhalla", description="Valkyries of the Valhalla host"
)
_midgard = stdgrimmsim.Population(
    id="Midgard", description="Valkyries patrolling the Midgard battlefields"
)


def _valhalla_host():
    id = "ValhallaHost_1D12"
    description = "Single population Valhalla Valkyrie model"
    long_description = """
        Single population of Valhalla valkyries. Modern N=12000,
        time=500 N=8000, time=3000 N=15000 (height of Viking battles),
        ancestral at time=8000 N=10000.
    """
    populations = [_valhalla]
    citations = [
        stdgrimmsim.Citation(
            author="Norse-Germanic tribal lore / Edda",
            year=900,
            doi="https://en.wikipedia.org/wiki/Valkyrie",
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
                initial_size=12_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=8_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=15_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_valhalla_host())


def _valhalla_midgard_split():
    id = "ValhallaMidgard_2D12"
    description = "Two population Valhalla-Midgard Valkyrie model"
    long_description = """
        Valhalla and Midgard valkyrie populations. Valhalla N=12000,
        Midgard N=8000. Split time=4000 from ancestral N=10000.
        Symmetric migration 3e-6.
    """
    populations = [_valhalla, _midgard]
    citations = [
        stdgrimmsim.Citation(
            author="Norse-Germanic tribal lore / Edda",
            year=900,
            doi="https://en.wikipedia.org/wiki/Valkyrie",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 3e-6],
        [3e-6, 0],
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
                initial_size=12_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=8_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=4_000, rate=0),
            msprime.MassMigration(time=4_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=4_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_valhalla_midgard_split())


def _christianization_decline():
    id = "Christianization_1D12"
    description = "Single population Valkyrie model with Christianization decline"
    long_description = """
        Single valkyrie population reflecting Christianization of Germanic
        tribes. Modern N=12000, time=200 N=2000 (post-conversion decline),
        time=500 N=15000 (pre-conversion peak), time=3000 N=10000,
        ancestral at time=8000 N=10000.
    """
    populations = [_valhalla]
    citations = [
        stdgrimmsim.Citation(
            author="Norse-Germanic tribal lore / Edda",
            year=900,
            doi="https://en.wikipedia.org/wiki/Valkyrie",
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
                initial_size=12_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=200, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=15_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=10_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=10_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_christianization_decline())
