import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("HexWal")
_brocken = stdgrimmsim.Population(
    id="Brocken", description="Witches of the Brocken summit (Harz)"
)
_bamberg = stdgrimmsim.Population(
    id="Bamberg", description="Witches of the Bamberg trials region"
)


def _brocken_sabbath():
    id = "BrockenSabbath_1D12"
    description = "Single population Brocken Walpurgis Witch model"
    long_description = """
        Single population of Brocken summit witches.
        Modern N=25000, witch trial persecution bottleneck 300 gen
        ago (N=5000), recovery 800 gen ago (N=20000), ancestral
        3000 gen ago (N=15000).
    """
    populations = [_brocken]
    citations = [
        stdgrimmsim.Citation(
            author="Goethe / German witch trial records",
            year=1690,
            doi="https://en.wikipedia.org/wiki/Walpurgis_Night",
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
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=300, initial_size=5_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=800, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_brocken_sabbath())


def _brocken_bamberg_split():
    id = "BrockenBamberg_2D12"
    description = "Two population Brocken-Bamberg Walpurgis Witch model"
    long_description = """
        Brocken and Bamberg witch populations. Ancestral N=15000.
        Split 2000 gen ago. Brocken 25000, Bamberg 15000.
        Symmetric migration 5e-6.
    """
    populations = [_brocken, _bamberg]
    citations = [
        stdgrimmsim.Citation(
            author="German witch trial records",
            year=1690,
            doi="https://en.wikipedia.org/wiki/Walpurgis_Night",
            reasons={stdgrimmsim.CiteReason.DEM_MODEL},
        )
    ]
    migration_matrix = [
        [0, 5e-6],
        [5e-6, 0],
    ]
    return stdgrimmsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=_species.generation_time,
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=15_000, metadata=populations[1].asdict()
            ),
        ],
        migration_matrix=migration_matrix,
        demographic_events=[
            msprime.MigrationRateChange(time=2_000, rate=0),
            msprime.MassMigration(time=2_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=2_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_brocken_bamberg_split())


def _witch_trial_purge():
    id = "WitchTrialPurge_1D12"
    description = (
        "Single population Walpurgis Witch model with severe witch-trial bottleneck"
    )
    long_description = """
        Single witch population with a severe bottleneck during the
        height of witch trials (~1690). Modern N=25000, height of
        trials 100 gen ago (N=1000), 300 gen ago (N=8000),
        800 gen ago (N=20000), ancestral 3000 gen ago (N=15000).
    """
    populations = [_brocken]
    citations = [
        stdgrimmsim.Citation(
            author="German witch trial records",
            year=1690,
            doi="https://en.wikipedia.org/wiki/Walpurgis_Night",
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
        mutation_rate=2.3e-8,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=25_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=100, initial_size=1_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=300, initial_size=8_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=800, initial_size=20_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=3_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_witch_trial_purge())
