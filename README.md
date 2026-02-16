# stdgrimmsim

[![PyPI version](https://img.shields.io/pypi/v/stdgrimmsim?color=8B7355)](https://pypi.org/project/stdgrimmsim/)
[![PyPI downloads](https://img.shields.io/pypi/dm/stdgrimmsim?color=6B5B4E)](https://pypi.org/project/stdgrimmsim/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/stdgrimmsim?color=5C4A3A)](https://pypi.org/project/stdgrimmsim/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-3C2F2F.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Docs](https://img.shields.io/github/actions/workflow/status/kevinkorfmann/stdgrimmsim/docs.yml?branch=main&label=docs&color=7A6652)](https://stdgrimmsim.readthedocs.io/en/latest/)
[![codecov](https://img.shields.io/codecov/c/gh/kevinkorfmann/stdgrimmsim?color=4A3C2A)](https://codecov.io/gh/kevinkorfmann/stdgrimmsim)
[![tests](https://img.shields.io/badge/tests-680%20passed-228B22)](https://github.com/kevinkorfmann/stdgrimmsim/actions/workflows/tests.yml)

**Install:** `pip install stdgrimmsim` · **Docs:** [stdgrimmsim.readthedocs.io](https://stdgrimmsim.readthedocs.io/en/latest/)

A community-maintained library of population genetic simulation models for
**German folklore, fairy tales, and mythology**, with a strong focus on **geographic regions**:
**Bavaria** (Bayern), **Prussia** (Preußen, East Prussia, Masuria), Rhine, Harz, Black Forest, and more.

Forked from [stdvoidsim](https://github.com/popsim-consortium/stdvoidsim) (and ultimately [stdpopsim](https://stdpopsim.org)),
`stdgrimmsim` provides fictional but population-genetically plausible demographic models
for creatures and spirits from German-speaking folklore. Demographics are tied to real regions (Upper Bavaria, Bavarian Forest, East Prussia, Kurische Nehrung, Masurian Lakes, etc.). All models use realistic population genetic parameters and are fully simulatable with `msprime` and `SLiM`.

**32 species, 150 demographic models** — **Bavaria**, **Prussia**, **Saxony**, **Pomerania**, **Lower Saxony/Bremen**, **Thuringia/Hesse**, and more Grimm fairy-tale species.

## Available Species

### Fairy tale & Grimm

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| ZweBerg | *Zwergus bergensis* | Bergzwerg (Mountain Dwarf) | 80,000 | 25 yr | 2 |
| FraHol | *Holle hesseensis* | Frau Holle (KHM 24) | 60,000 | 30 yr | 2 |
| KobHau | *Koboldus domesticus* | Kobold (house spirit) | 200,000 | 15 yr | 2 |
| HeiCol | *Heinzelmaennchen coloniensis* | Heinzelmännchen (Cologne) | 300,000 | 8 yr | 2 |
| RumSti | *Rumpelstilzchen thuringiensis* | Rumpelstiltskin (KHM 55) | 48,000 | 22 yr | 2 |
| SieRab | *Corvus septem ravens* | Seven Ravens (KHM 25) | 65,000 | 18 yr | 2 |
| BreSta | *Bremer stadtmusikanten* | Town Musicians of Bremen (KHM 27) | 88,000 | 14 yr | 2 |
| AscPut | *Aschenputtel doves* | Cinderella doves (KHM 21) | 420,000 | 8 yr | 2 |

### Water & river spirits

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| NixRhe | *Nixus rhenanus* | Nix (Rhine water spirit) | 45,000 | 50 yr | 2 |
| LorRhe | *Loreley rhenanus* | Loreley (Rhine rock spirit) | 35,000 | 40 yr | 2 |
| FeeFlu | *Flussfee aquaticus* | Flussfee (River Fairy) | 55,000 | 30 yr | 2 |

### Bavaria (Bayern)

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| WolBay | *Wolpertingerus bavarius* | Wolpertinger (Bavarian hybrid) | 95,000 | 12 yr | 2 |
| BerAlp | *Berchta alpina* | Berchta / Perchta (Alpine winter) | 42,000 | 35 yr | 2 |
| MooBay | *Moosweib bavaricum* | Moosweib (Bavarian Forest) | 38,000 | 28 yr | 2 |

Demographic models use **Upper Bavaria (Oberbayern)**, **Bavarian Forest (Bayrischer Wald)**, **Allgäu**, **Salzburg**, **Tyrol**, **Oberpfalz**.

### Prussia (Preußen)

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| PukPru | *Puk prussicus* | Puk (Prussian house spirit) | 180,000 | 18 yr | 2 |
| OstBal | *Ostpreussius balticus* | East Prussian Baltic spirit | 28,000 | 55 yr | 2 |
| MasLak | *Masurius lacustris* | Masurian lake spirit (Masuren) | 32,000 | 48 yr | 2 |

Demographic models use **East Prussia (Ostpreußen)**, **West Prussia**, **Berlin–Brandenburg**, **Kurische Nehrung (Curonian Spit)**, **Memelland**, **Samland**, **Masurian Lakes**, **Spirdingsee (Śniardwy)**, **Mauersee (Mamry)**.

### Saxony (Sachsen) & Pomerania (Pommern)

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| SaxErz | *Bergmann erzgebirgensis* | Erzgebirge spirit (Ore Mountains) | 72,000 | 28 yr | 2 |
| PomBal | *Pommersch balticus* | Pomeranian Baltic spirit | 36,000 | 52 yr | 2 |

Demographic models use **Erzgebirge**, **Vogtland**, **Dresden region** (Saxony); **Usedom**, **Rügen**, **Stettin** (Pomeranian Baltic).

### Thuringia & Hesse (Grimm heartland)

Rumpelstiltskin (RumSti) and other Grimm species use **Thuringia (Thüringen)** and **Hesse (Hessen)** populations — the core Grimm fairy-tale region.

### Lower Saxony & Bremen

Town Musicians of Bremen (BreSta) use **Bremen**, **Lower Saxony (Niedersachsen)**, **Lüneburg Heath (Lüneburger Heide)**.

### Mountain & regional mythology

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| RueHar | *Ruebezahl harzensis* | Rübezahl (mountain spirit) | 15,000 | 100 yr | 2 |
| SchWar | *Silvani schwarzwaldensis* | Black Forest spirit | 120,000 | 20 yr | 2 |
| LinDra | *Lindwurm draconicus* | Lindwurm (Dragon) | 2,000 | 200 yr | 2 |

### Beings & hauntings

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| WilJae | *Wildjaeger germanicus* | Wilde Jagd (Wild Hunt) | 25,000 | 60 yr | 2 |
| WerWol | *Werwolfus lupinus* | Werwolf (Werewolf) | 10,000 | 20 yr | 2 |
| ErlKoe | *Erlkoenig sylvestris* | Erlkönig (Alder King) | 30,000 | 45 yr | 2 |
| AlpNac | *Alpus nocturnalis* | Alp (nightmare spirit) | 150,000 | 10 yr | 2 |

### Dragons & medieval bestiary

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| LinDra | *Lindwormis draco* | Lindworm (dragon) | 5,000 | 60 yr | 2 |
| DraFeu | *Draco feuerspeiensis* | Firedrake (fire dragon) | 8,000 | 50 yr | 2 |
| BasRex | *Basiliscus rex* | Basilisk (serpent king) | 5,000 | 80 yr | 2 |

### Pre-Christian & tribal Germanic

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| JotRie | *Jotunnus riesensis* | Frost Giant (Jotun) | 3,000 | 150 yr | 2 |
| ValKri | *Valkyria kriegensis* | Valkyrie (battle chooser) | 12,000 | 100 yr | 2 |

### 17th-18th century folklore

| ID | Species | Common Name | Pop Size | Gen Time | Ploidy |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| HexWal | *Hexara walpurgis* | Walpurgis Witch (Brocken) | 25,000 | 30 yr | 2 |
| MueGei | *Muellerin geisterhaft* | Mill Ghost (Mühlengeist) | 40,000 | 20 yr | 2 |

## Quick Start

```python
import stdgrimmsim

# Get the mountain dwarf species (Schwarzwald / Harz)
species = stdgrimmsim.get_species("ZweBerg")

# Use the Black Forest single-population demographic model
model = species.get_demographic_model("BlackForest_1D12")

# Set up a generic contig of 100kb
contig = species.get_contig(length=100_000)

# Simulate with msprime
engine = stdgrimmsim.get_engine("msprime")
ts = engine.simulate(model, contig, samples={"BlackForest": 20}, seed=42)

print(f"Trees: {ts.num_trees}, Mutations: {ts.num_mutations}")
```

## CLI Usage

```bash
# List all available species
stdgrimmsim --help

# Simulate 10 Black Forest dwarf samples
stdgrimmsim ZweBerg -d BlackForest_1D12 -o dwarves.trees -L 100000 BlackForest:10

# Simulate Nix (water spirit) from Rhine and Elbe
stdgrimmsim NixRhe -d RhineElbe_2D12 -o nix.trees -L 50000 Rhine:10 Elbe:10

# Bavaria: Wolpertinger (Upper Bavaria + Bavarian Forest)
stdgrimmsim WolBay -d UpperBavariaBavarianForest_2D12 -o wolpertinger.trees -L 50000 UpperBavaria:10 BavarianForest:10

# Prussia: Puk (East Prussia and Berlin–Brandenburg)
stdgrimmsim PukPru -d EastPrussiaBerlinBrandenburg_2D12 -o puk.trees -L 50000 EastPrussia:10 BerlinBrandenburg:10
```

## Installation

From PyPI (once published):

```bash
pip install stdgrimmsim
```

From source (editable):

```bash
pip install -e .
```

### SLiM engine (optional)

To run simulations with the **SLiM** engine instead of msprime, install [SLiM](https://messerlab.org/slim/) and ensure `slim` is on your `PATH`. Use **SLiM 3.x** (e.g. 3.7); the generated scripts target the SLiM 3 API.

```bash
stdgrimmsim ZweBerg -d BlackForest_1D12 -e slim -o dwarves.trees -L 10000 BlackForest:10
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
  that reflect regional folklore and fairy-tale settings (Bavaria, Prussia, Black Forest, Harz, Rhine, Masuria, etc.)
- **Simulatable parameters**: all values are chosen so that simulations complete in
  reasonable time and produce meaningful coalescent trees

The models are designed to be useful for testing population genetic inference methods
on non-standard demographic scenarios (bottlenecks, splits, migrations) in a fun,
folklore-themed setting.

## Citation

This project is a fork of [stdvoidsim](https://github.com/popsim-consortium/stdvoidsim) and [stdpopsim](https://stdpopsim.org).
If you use the simulation framework, please cite:

* [Adrion, et al. (2020)](https://doi.org/10.7554/eLife.54967)
* [Lauterbur, et al. (2023)](https://doi.org/10.7554/eLife.84874)

*"Es war einmal …"*
