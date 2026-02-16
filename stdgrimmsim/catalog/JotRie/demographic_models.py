import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("JotRie")
_niflheim = stdgrimmsim.Population(
    id="Niflheim", description="Frost Giants of the northern wastes (Niflheim)"
)
_jotunheim = stdgrimmsim.Population(
    id="Jotunheim", description="Frost Giants of the mountain realm (Jotunheim)"
)


def _niflheim_clan():
    id = "NiflheimClan_1D12"
    description = "Single population Niflheim Frost Giant model"
    long_description = """
        Single population of Frost Giants in Niflheim.
        Modern N=3000, time=500 N=2000, time=2000 N=4000,
        ancestral at time=10000 N=5000.
    """
    populations = [_niflheim]
    citations = [
        stdgrimmsim.Citation(
            author="Snorri Sturluson / Germanic tribal lore",
            year=800,
            doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
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
        mutation_rate=1.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=500, initial_size=2_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=4_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_niflheim_clan())


def _nifl_jotun_split():
    id = "NiflJotun_2D12"
    description = "Two population Niflheim-Jotunheim Frost Giant model"
    long_description = """
        Niflheim and Jotunheim Frost Giant populations. Ancestral N=5000.
        Split 5000 gen ago. Niflheim N=3000, Jotunheim N=2000.
        Symmetric migration 5e-7.
    """
    populations = [_niflheim, _jotunheim]
    citations = [
        stdgrimmsim.Citation(
            author="Snorri Sturluson / Germanic tribal lore",
            year=800,
            doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
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
        mutation_rate=1.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=2_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=5_000, rate=0),
            msprime.MassMigration(
                time=5_000, source=1, destination=0, proportion=1.0
            ),
            msprime.PopulationParametersChange(
                time=5_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_nifl_jotun_split())


def _ragnarok():
    id = "Ragnarok_1D12"
    description = "Single population Frost Giant model with Ragnarok bottleneck"
    long_description = """
        Single Frost Giant population with cataclysmic Ragnarok decline.
        Modern N=3000, time=100 N=200 (Ragnarok bottleneck),
        time=500 N=1500, time=3000 N=5000, ancestral at time=10000 N=5000.
    """
    populations = [_niflheim]
    citations = [
        stdgrimmsim.Citation(
            author="Snorri Sturluson / Germanic tribal lore",
            year=800,
            doi="https://en.wikipedia.org/wiki/J%C3%B6tunn",
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
        mutation_rate=1.0e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=3_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=100, initial_size=200, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=500, initial_size=1_500, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=5_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=5_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_ragnarok())
