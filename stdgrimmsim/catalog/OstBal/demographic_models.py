import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("OstBal")
_kurische_nehrung = stdgrimmsim.Population(
    id="KurischeNehrung", description="Spirits of the Curonian Spit (Kurische Nehrung)"
)
_memelland = stdgrimmsim.Population(
    id="Memelland", description="Spirits of the Memel region (Memelland / Klaipėda)"
)
_samland = stdgrimmsim.Population(
    id="Samland", description="Spirits of Samland (Königsberg peninsula)"
)


def _kurische_nehrung_single():
    id = "KurischeNehrung_1D12"
    description = "Single population Curonian Spit (Kurische Nehrung) model"
    long_description = """
        Single population on the Curonian Spit (Kurische Nehrung), East Prussia.
        Modern N=28000, bottleneck 1500 gen ago (N=6000),
        ancestral 20000 gen ago (N=15000).
    """
    populations = [_kurische_nehrung]
    citations = [
        stdgrimmsim.Citation(
            author="East Prussian / Baltic folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/Curonian_Spit",
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
                initial_size=28_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=1_500, initial_size=6_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=20_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_kurische_nehrung_single())


def _kurische_memel_split():
    id = "KurischeNehrungMemelland_2D12"
    description = "Two population Curonian Spit and Memelland model"
    long_description = """
        Kurische Nehrung and Memelland (Memel delta / Klaipėda). Ancestral N=15000.
        Split 10000 gen ago. Curonian Spit 28000, Memelland 18000.
    """
    populations = [_kurische_nehrung, _memelland]
    citations = [
        stdgrimmsim.Citation(
            author="East Prussian folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/East_Prussia",
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
                initial_size=28_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=10_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=10_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_kurische_memel_split())


def _east_prussia_three_region():
    id = "EastPrussiaBaltic_3D12"
    description = "Three population East Prussian Baltic: Nehrung, Memelland, Samland"
    long_description = """
        Three East Prussian Baltic regions. Ancestral N=15000. Splits: Samland 12000 gen ago,
        Memelland 18000 gen ago. Kurische Nehrung 28000, Memelland 18000, Samland 22000.
    """
    populations = [_kurische_nehrung, _memelland, _samland]
    citations = [
        stdgrimmsim.Citation(
            author="East Prussian folklore",
            year=1800,
            doi="https://en.wikipedia.org/wiki/East_Prussia",
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
                initial_size=28_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=18_000, metadata=populations[1].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=22_000, metadata=populations[2].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=12_000, source=2, destination=0, proportion=1.0),
            msprime.MassMigration(time=18_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=18_000, initial_size=15_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_east_prussia_three_region())
