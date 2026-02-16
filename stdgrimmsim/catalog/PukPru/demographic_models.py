import msprime
import stdgrimmsim

_species = stdgrimmsim.get_species("PukPru")
_east_prussia = stdgrimmsim.Population(
    id="EastPrussia", description="Puk of East Prussia (Ostpreußen)"
)
_west_prussia = stdgrimmsim.Population(
    id="WestPrussia", description="Puk of West Prussia (Westpreußen)"
)
_berlin_brandenburg = stdgrimmsim.Population(
    id="BerlinBrandenburg", description="Puk of Berlin and Brandenburg"
)


def _east_prussia_single():
    id = "EastPrussia_1D12"
    description = "Single population East Prussia Puk model"
    long_description = """
        Single population in East Prussia (Königsberg, Memelland, Baltic).
        Modern N=180000 (pre-1945 range), bottleneck 2000 gen ago (N=40000),
        ancestral 25000 gen ago (N=90000).
    """
    populations = [_east_prussia]
    citations = [
        stdgrimmsim.Citation(
            author="Prussian folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Puk_(mythology)",
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
                initial_size=180_000, metadata=populations[0].asdict()
            )
        ],
        demographic_events=[
            msprime.PopulationParametersChange(
                time=2_000, initial_size=40_000, population_id=0
            ),
            msprime.PopulationParametersChange(
                time=25_000, initial_size=90_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_east_prussia_single())


def _east_west_prussia_split():
    id = "EastPrussiaWestPrussia_2D12"
    description = "Two population East and West Prussia Puk model"
    long_description = """
        East Prussia (Ostpreußen) and West Prussia (Westpreußen / Pomerelia).
        Ancestral N=90000. Split 12000 gen ago. East Prussia 180000, West Prussia 70000.
    """
    populations = [_east_prussia, _west_prussia]
    citations = [
        stdgrimmsim.Citation(
            author="Prussian folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Puk_(mythology)",
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
                initial_size=180_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=70_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=12_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=12_000, initial_size=90_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_east_west_prussia_split())


def _prussia_brandenburg_split():
    id = "EastPrussiaBerlinBrandenburg_2D12"
    description = "Two population East Prussia and Berlin–Brandenburg model"
    long_description = """
        East Prussia and Berlin–Brandenburg (core Prussia). Ancestral N=90000.
        Split 8000 gen ago. East Prussia 180000, Berlin–Brandenburg 120000.
    """
    populations = [_east_prussia, _berlin_brandenburg]
    citations = [
        stdgrimmsim.Citation(
            author="Prussian folklore",
            year=1700,
            doi="https://en.wikipedia.org/wiki/Puk_(mythology)",
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
                initial_size=180_000, metadata=populations[0].asdict()
            ),
            msprime.PopulationConfiguration(
                initial_size=120_000, metadata=populations[1].asdict()
            ),
        ],
        demographic_events=[
            msprime.MassMigration(time=8_000, source=1, destination=0, proportion=1.0),
            msprime.PopulationParametersChange(
                time=8_000, initial_size=90_000, population_id=0
            ),
        ],
    )


_species.add_demographic_model(_prussia_brandenburg_split())
