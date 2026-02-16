# stdvoidsim

[![PyPI version](https://img.shields.io/pypi/v/stdvoidsim)](https://pypi.org/project/stdvoidsim/)
[![PyPI downloads](https://img.shields.io/pypi/dm/stdvoidsim)](https://pypi.org/project/stdvoidsim/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/stdvoidsim)](https://pypi.org/project/stdvoidsim/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Docs](https://github.com/kevinkorfmann/stdvoidsim/actions/workflows/docs.yml/badge.svg?branch=main)](https://stdvoidsim.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/kevinkorfmann/stdvoidsim/graph/badge.svg)](https://codecov.io/gh/kevinkorfmann/stdvoidsim)

**Install:** `pip install stdvoidsim` · **Docs:** [stdvoidsim.readthedocs.io](https://stdvoidsim.readthedocs.io/en/latest/)

A community-maintained library of population genetic simulation models for
**Lovecraftian entities and eldritch horrors**.

Built on the [stdvoidsim](https://github.com/popsim-consortium/stdvoidsim) framework,
`stdvoidsim` provides fictional but population-genetically plausible demographic models
for creatures from H.P. Lovecraft's Cthulhu Mythos. All models use realistic population
genetic parameters and are fully simulatable with `msprime` and `SLiM`.

**40 species, 80 demographic models.**

## Available Species

### Outer Gods & Great Old Ones

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| AzaPri | *Azathoth primordia* | Blind Idiot God | 1 | 1M yr | 2 |
| CthGre | *Cthulhu greatoldone* | Great Cthulhu | 500 | 10K yr | 4 |
| DagGod | *Dagonus maximus* | Father Dagon | 50 | 50K yr | 4 |
| HasKin | *Hastur carcosensis* | King in Yellow | 2,000 | 50 yr | 2 |
| NyaAza | *Nyarlathotep azathothspawn* | Crawling Chaos | 1,000 | 1 yr | 2 |
| ShbNig | *Shubniggurath fertilitas* | Black Goat of the Woods | 100,000 | 25 yr | 2 |
| TsaGod | *Tsathoggua somnolentis* | Tsathoggua | 100 | 50K yr | 2 |
| YogSot | *Yogsothoth dimensionalis* | The Key and the Gate | 10 | 100K yr | 2 |
| ChaFau | *Chaugnarus faugnis* | Chaugnar Faugn | 200 | 10K yr | 2 |

### Servitor Races & Engineered Species

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| ShoNig | *Shoggoth nigrumplasma* | Shoggoth | 100,000 | 0.5 yr | 6 |
| StarSp | *Starspawn cthulhidae* | Star-Spawn of Cthulhu | 10,000 | 5K yr | 4 |
| DarYou | *Obscurus silvanus* | Dark Young | 35,000 | 50 yr | 3 |
| ForSpa | *Informis generatus* | Formless Spawn | 25,000 | 10 yr | 2 |
| HunTin | *Venator obscurus* | Hunting Horror | 15,000 | 20 yr | 2 |
| FirVam | *Igneus vampirus* | Fire Vampire | 1M | 0.01 yr | 1 |
| BybWor | *Byakhee voidwing* | Byakhee | 200,000 | 10 yr | 2 |

### Ancient Civilizations

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| EldThi | *Elderium antarcticae* | Elder Thing | 10,000 | 1K yr | 2 |
| YitGre | *Yithianus temporalis* | Great Race of Yith | 50,000 | 500 yr | 2 |
| FlyPol | *Polypus volantis* | Flying Polyp | 20,000 | 2K yr | 2 |
| SerHum | *Serpentis valusiensis* | Serpent Person | 40,000 | 50 yr | 2 |
| MiGFun | *Migo fungoides* | Fungi from Yuggoth | 500,000 | 5 yr | 2 |

### Amphibious & Aquatic

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| DagHyd | *Dagonus hydridae* | Deep One | 50,000 | 100 yr | 2 |
| ColOos | *Chromatis extraspatiala* | Colour Out of Space | 10,000 | 0.1 yr | 1 |

### Subterranean Horrors

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| GhoFee | *Ghoulish necrophagus* | Ghoul | 30,000 | 20 yr | 2 |
| GugsUn | *Gugus underworldis* | Gug | 25,000 | 30 yr | 2 |
| GhaShe | *Ghastus cavernicola* | Ghast | 80,000 | 3 yr | 2 |
| DhoGno | *Dholos subterraneus* | Dhole | 15,000 | 200 yr | 2 |
| WamUnd | *Degeneratus subterraneus* | Wamp | 20,000 | 10 yr | 2 |

### Dreamlands Creatures

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| NigMan | *Nightgauntus mantaformis* | Nightgaunt | 75,000 | 5 yr | 2 |
| SanDre | *Shantakus dreamlandis* | Shantak | 60,000 | 15 yr | 2 |
| MooFun | *Lunaris bestialis* | Moon-Beast | 45,000 | 8 yr | 2 |
| ZooGul | *Zoogus sylvaticus* | Zoog | 500,000 | 2 yr | 2 |
| CatUlt | *Felis ultharensis* | Cat of Ulthar | 100,000 | 5 yr | 2 |
| LenSpi | *Araneus lengensis* | Leng Spider | 20,000 | 10 yr | 2 |

### Interdimensional & Temporal

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| HouFir | *Houndus tindalosi* | Hound of Tindalos | 5,000 | 500 yr | 2 |
| DimSha | *Dimensius shambleris* | Dimensional Shambler | 3,000 | 100 yr | 2 |

### Arctic & Desert

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| GnpKeh | *Gnophkehus arcticus* | Gnoph-Keh | 12,000 | 40 yr | 2 |
| SanDwl | *Arenicola abyssalis* | Sand Dweller | 40,000 | 15 yr | 2 |

### Human-Adjacent Horrors

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| TsaCho | *Tsathoggua choriensis* | Tcho-Tcho | 70,000 | 25 yr | 2 |
| RatThi | *Rattus magicus* | Rat-Thing | 50,000 | 1 yr | 2 |

## Quick Start

```python
import stdvoidsim

# Get the Shoggoth species (hexaploid engineered servitors)
species = stdvoidsim.get_species("ShoNig")

# Use the Antarctic Revolt demographic model
model = species.get_demographic_model("AntarcticRevolt_1D31")

# Set up a generic contig of 100kb
contig = species.get_contig(length=100_000)

# Simulate with msprime
engine = stdvoidsim.get_engine("msprime")
ts = engine.simulate(model, contig, samples={"Antarctic": 20}, seed=42)

print(f"Trees: {ts.num_trees}, Mutations: {ts.num_mutations}")
```

## CLI Usage

```bash
# List all available species
stdvoidsim --help

# Simulate 10 Deep One samples under the Innsmouth Decline model
stdvoidsim DagHyd -d InnsmouthDecline_1M27 -o deep_ones.trees -L 100000 DeepOnes:10

# Simulate Shoggoth rebellion scenario
stdvoidsim ShoNig -d AntarcticRevolt_1D31 -o shoggoths.trees -L 50000 Shoggoth:20
```

## Installation

From PyPI (once published):

```bash
pip install stdvoidsim
```

From source (editable):

```bash
pip install -e .
```

### SLiM engine (optional)

To run simulations with the **SLiM** engine instead of msprime, install [SLiM](https://messerlab.org/slim/) and ensure `slim` is on your `PATH`. Use **SLiM 3.x** (e.g. 3.7); the generated scripts target the SLiM 3 API. SLiM 4.x changed the API (e.g. `initializeSex()`); the engine may need updates for full SLiM 4 support. The SLiM engine supports **ploidy 1 or 2 only**; species with higher ploidy (e.g. Cthulhu 4, Shoggoth 6) must be simulated with the msprime engine.

```bash
# Example: Deep Ones with SLiM (diploid)
stdvoidsim DagHyd -d InnsmouthDecline_1M27 -e slim -o deep_ones.trees -L 10000 DeepOnes:10
```

### Development with uv

[uv](https://github.com/astral-sh/uv) makes installing and running tests fast. Install uv (`pip install uv` or `brew install uv`), then from the repo root:

```bash
make install    # editable install + dev/CI dependencies
make test       # run test suite
make test-cov   # run tests with coverage
make quick-sim  # run quick simulation check (.test/run_simulation.py)
```

Or without Make: `uv pip install -e .`, `uv pip install -r requirements/CI/requirements.txt`, then `uv run pytest -v tests`.

### Releasing to PyPI

The package uses [setuptools_scm](https://github.com/pypa/setuptools_scm) for versioning; the version is read from git tags. To publish a release to PyPI:

1. **One-time:** Create a PyPI account and an API token at [pypi.org/manage/account/token/](https://pypi.org/manage/account/token/). Add the token as repository secret `PYPI_API_TOKEN` in GitHub (Settings → Secrets and variables → Actions).
2. **Each release:** Tag the commit with a semantic version and push. The GitHub Action will build and upload to PyPI:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
   Use a new tag for each release (e.g. `v0.1.1`, `v0.2.0`). To test without publishing, use [Test PyPI](https://test.pypi.org/) and set `TWINE_REPOSITORY_URL` in the workflow or run `twine upload --repository-url https://test.pypi.org/legacy/ dist/*` locally.

## Design Philosophy

Each species has:
- **Made-up but internally consistent genome**: chromosome counts, lengths, ploidy,
  mutation rates, and recombination rates chosen to reflect the creature's biology
- **Demographic models**: population size changes, bottlenecks, splits, and migrations
  that tell a story consistent with the Mythos lore
- **Simulatable parameters**: all values are chosen so that simulations complete in
  reasonable time and produce meaningful coalescent trees

The models are designed to be useful for testing population genetic inference methods
on non-standard demographic scenarios (extreme bottlenecks, very small populations,
polyploidy, highly asymmetric migration, etc.).

## Citation

This project is a fork of [stdvoidsim](https://github.com/popsim-consortium/stdvoidsim).
If you use the simulation framework, please cite:

* [Adrion, et al. (2020)](https://doi.org/10.7554/eLife.54967)
* [Lauterbur, et al. (2023)](https://doi.org/10.7554/eLife.84874)

*"Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn."*
# stdgrimmsim
