import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("PomBal")
_usedom = stdgrimmsim.Population(
    id="Usedom", description="Spirits of Usedom island (Pomerania)"
)
_rugen = stdgrimmsim.Population(
    id="Rugen", description="Spirits of Rügen island"
)
_stettin = stdgrimmsim.Population(
    id="Stettin", description="Stettin (Szczecin) lagoon and Oder mouth"
)


def _usedom_single():
    id = "Usedom_1D12"
    description = "Single population Usedom (Pomeranian Baltic) model"
    long_description = """
        Single population on Usedom (Pomeranian coast / Baltic).
        Modern N=36000, expansion 2500 gen ago (N=16000),
        ancestral 18000 gen ago (N=12000).
    """
    populations = [_usedom]
    citations = [
        stdgrimmsim.Citation(
            author="Pomeranian folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Pomerania",
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
                initial_size=36_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2_500, initial_size=16_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=12_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_usedom_single())


def _usedom_rugen_split():
    id = "UsedomRugen_2D12"
    description = "Two population Usedom and Rügen (Pomeranian islands)"
    long_description = """
        Usedom and Rügen — two major Baltic islands of Pomerania.
        Ancestral N=12000. Split 8000 gen ago. Usedom 36000, Rügen 24000.
    """
    populations = [_usedom, _rugen]
    citations = [
        stdgrimmsim.Citation(
            author="Pomeranian folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Pomerania",
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
                initial_size=36_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=24_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=12_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_usedom_rugen_split())


def _pomerania_three_region():
    id = "PomeraniaBaltic_3D12"
    description = "Three population Pomeranian Baltic: Usedom, Rügen, Stettin"
    long_description = """
        Usedom, Rügen, and Stettin lagoon (Szczecin / Oder). Ancestral N=12000.
        Splits: Stettin 6000 gen ago, Rügen 12000 gen ago.
    """
    populations = [_usedom, _rugen, _stettin]
    citations = [
        stdgrimmsim.Citation(
            author="Pomeranian folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Pomerania",
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
                initial_size=36_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=24_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=28_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=6_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=12_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_pomerania_three_region())
