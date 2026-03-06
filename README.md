# stdgrimmsim

[![PyPI version](https://img.shields.io/pypi/v/stdgrimmsim?color=8B7355)](https://pypi.org/project/stdgrimmsim/)
[![PyPI downloads](https://img.shields.io/pypi/dm/stdgrimmsim?color=6B5B4E)](https://pypi.org/project/stdgrimmsim/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/stdgrimmsim?color=5C4A3A)](https://pypi.org/project/stdgrimmsim/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-3C2F2F.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Docs](https://img.shields.io/github/actions/workflow/status/kevinkorfmann/stdgrimmsim/docs.yml?branch=main&label=docs&color=7A6652)](https://stdgrimmsim.readthedocs.io/en/latest/)
[![codecov](https://img.shields.io/codecov/c/gh/kevinkorfmann/stdgrimmsim?color=4A3C2A)](https://codecov.io/gh/kevinkorfmann/stdgrimmsim)
[![tests](https://img.shields.io/github/actions/workflow/status/kevinkorfmann/stdgrimmsim/tests.yml?branch=main&label=tests)](https://github.com/kevinkorfmann/stdgrimmsim/actions/workflows/tests.yml)

**Install:** `pip install stdgrimmsim` · **Docs:** [stdgrimmsim.readthedocs.io](https://stdgrimmsim.readthedocs.io/en/latest/)

A community-maintained library of population genetic simulation models for
**German folklore, fairy tales (Grimm), and regional mythology**.

**32 species · 150 demographic models** across 4 complexity levels.

> See also: [**stdvoidsim**](https://github.com/kevinkorfmann/stdvoidsim) — the companion catalog for stress-testing with extreme Lovecraftian scenarios.

## Purpose

`stdgrimmsim` is a *fork catalog* of [stdpopsim](https://stdpopsim.org): it shares the same API and simulation engines (msprime, SLiM) but replaces the species catalog with fictional taxa from German folklore.

**Primary use case: generating diverse, plausible training data** for ML/DL-based population-genetic inference methods and for systematic parameter-space benchmarking.

All species are diploid with demographically plausible parameters (Ne from 2,000 to 420,000; generation times 8–200 years). Demographies are tied to **geographic regions** (Black Forest, Harz, Rhine, Bavaria, Prussia, Saxony) and **folkloric narratives** (Frau Holle's well, Rubezahl's mountain, the Loreley rock), making simulations easy to remember and cite.

| | stdgrimmsim | stdvoidsim |
|---|---|---|
| **Focus** | Diverse training data & benchmarking | Stress-testing & identifiability limits |
| **Species** | 32 (German folklore) | 40 (Cthulhu Mythos) |
| **Models** | 150 (1- to 4-population) | 82 (1- and 2-population) |
| **Parameter range** | Moderate, plausible | Extreme (Ne=1 to 10^6, gen. time 0.01–10^6 yr) |
| **Ploidy** | All diploid | Diploid to hexaploid |

## Model Complexity Taxonomy

Models are organized by population count, allowing systematic sweeps over complexity:

| Level | Type | Count | Examples |
|-------|------|-------|----------|
| **1** | 1-population (constant or piecewise) | 68 | `BlackForest_1D12`, `WellRealm_1D12`, `Rhine_1D12` |
| **2** | 2-population (split ± migration) | 48 | `HarzBlackForest_2D12`, `RhineElbe_2D12`, `WellSnow_2D12` |
| **3** | 3-population | 20 | `ThreeRivers_3D12`, `ThreeForestRealms_3D12` |
| **4** | 4-population | 14 | `FourMountainRanges_4D12`, `FourRealms_4D12` |

## Available Species

### Fairy tale & Grimm

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| ZweBerg | *Zwergus bergensis* | Bergzwerg (Mountain Dwarf) | 80,000 | 25 yr | 7 |
| FraHol | *Holle hesseensis* | Frau Holle (KHM 24) | 60,000 | 30 yr | 7 |
| KobHau | *Koboldus domesticus* | Kobold (house spirit) | 200,000 | 15 yr | 7 |
| HeiCol | *Heinzelmaennchen coloniensis* | Heinzelmannchen (Cologne) | 300,000 | 8 yr | 8 |
| RumSti | *Rumpelstilzchen thuringiensis* | Rumpelstiltskin (KHM 55) | 48,000 | 22 yr | 2 |
| SieRab | *Corvus septem ravens* | Seven Ravens (KHM 25) | 65,000 | 18 yr | 2 |
| BreSta | *Bremer stadtmusikanten* | Town Musicians of Bremen (KHM 27) | 88,000 | 14 yr | 3 |
| AscPut | *Aschenputtel doves* | Cinderella doves (KHM 21) | 420,000 | 8 yr | 2 |

### Water & river spirits

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| NixRhe | *Nixus rhenanus* | Nix (Rhine water spirit) | 45,000 | 50 yr | 7 |
| LorRhe | *Loreley rhenanus* | Loreley (Rhine rock spirit) | 35,000 | 40 yr | 7 |
| FeeFlu | *Flussfee aquaticus* | Flussfee (River Fairy) | 55,000 | 30 yr | 8 |

### Forest & nocturnal spirits

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| ErlKoe | *Erlkoenig sylvestris* | Erlkoenig (Alder King) | 30,000 | 45 yr | 7 |
| AlpNac | *Alpus nocturnalis* | Alp (nightmare spirit) | 150,000 | 10 yr | 7 |
| WilJae | *Wildjaeger germanicus* | Wilde Jagd (Wild Hunt) | 25,000 | 60 yr | 7 |
| MueGei | *Muellerin geisterhaft* | Mill Ghost (Muhlengeist) | 40,000 | 20 yr | 3 |

### Mountain & regional mythology

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| RueHar | *Ruebezahl harzensis* | Rubezahl (mountain spirit) | 15,000 | 100 yr | 7 |
| SchWar | *Silvani schwarzwaldensis* | Black Forest spirit | 120,000 | 20 yr | 7 |
| SaxErz | *Bergmann erzgebirgensis* | Erzgebirge spirit (Ore Mtn.) | 72,000 | 28 yr | 3 |

### Bavaria (Bayern)

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| WolBay | *Wolpertingerus bavarius* | Wolpertinger | 95,000 | 12 yr | 3 |
| BerAlp | *Berchta alpina* | Berchta / Perchta | 42,000 | 35 yr | 3 |
| MooBay | *Moosweib bavaricum* | Moosweib (moss woman) | 38,000 | 28 yr | 2 |

### Prussia (Preussen)

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| PukPru | *Puk prussicus* | Puk (house spirit) | 180,000 | 18 yr | 3 |
| OstBal | *Ostpreussius balticus* | East Prussian Baltic spirit | 28,000 | 55 yr | 3 |
| MasLak | *Masurius lacustris* | Masurian lake spirit | 32,000 | 48 yr | 3 |

### Pomerania (Pommern)

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| PomBal | *Pommersch balticus* | Pomeranian Baltic spirit | 36,000 | 52 yr | 3 |

### Shape-shifters & mythical beasts

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| WerWol | *Werwolfus lupinus* | Werewolf | 10,000 | 20 yr | 7 |
| LinDra | *Lindwurm draconicus* | Lindwurm (dragon) | 2,000 | 200 yr | 7 |
| DraFeu | *Draco feuerspeiensis* | Firedrake (fire dragon) | 8,000 | 50 yr | 3 |
| BasRex | *Basiliscus rex* | Basilisk (serpent king) | 5,000 | 80 yr | 3 |

### Pre-Christian & Germanic mythology

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| JotRie | *Jotunnus riesensis* | Frost Giant (Jotun) | 3,000 | 150 yr | 3 |
| ValKri | *Valkyria kriegensis* | Valkyrie (battle chooser) | 12,000 | 100 yr | 3 |

### 17th–18th century folklore

| ID | Species | Common Name | Ne | Gen Time | Models |
|--------|-------------------------------|--------------------------|----------|----------|--------|
| HexWal | *Hexara walpurgis* | Walpurgis Witch (Brocken) | 25,000 | 30 yr | 3 |

## Quick Start

```python
import stdgrimmsim

# Get the mountain dwarf species
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

# Level 1: single-population model
stdgrimmsim ZweBerg -d BlackForest_1D12 -o dwarves.trees -L 100000 BlackForest:10

# Level 2: two-population split with migration
stdgrimmsim NixRhe -d RhineElbe_2D12 -o nix.trees -L 50000 Rhine:10 Elbe:10

# Level 3: three-population model
stdgrimmsim NixRhe -d ThreeRivers_3D12 -o nix3.trees -L 50000 Rhine:10 Elbe:10 Danube:10

# Level 4: four-population model
stdgrimmsim ZweBerg -d FourMountainRanges_4D12 -o dwarves4.trees -L 50000 BlackForest:5 Harz:5 Alps:5 Erzgebirge:5
```

## Installation

```bash
pip install stdgrimmsim
```

From source (editable):

```bash
pip install -e .
```

### SLiM engine (optional)

To run simulations with **SLiM** instead of msprime, install [SLiM](https://messerlab.org/slim/) and ensure `slim` is on your `PATH`. Use **SLiM 3.x**.

```bash
stdgrimmsim ZweBerg -d BlackForest_1D12 -e slim -o dwarves.trees -L 10000 BlackForest:10
```

### Development with uv

```bash
make install    # editable install + dev/CI dependencies
make test       # run test suite
make test-cov   # run tests with coverage
make quick-sim  # run quick simulation check
```

## Citation

This project is a fork of [stdpopsim](https://stdpopsim.org). If you use the simulation framework, please cite:

* [Adrion, et al. (2020)](https://doi.org/10.7554/eLife.54967) — A community-maintained standard library of population genetic models.
* [Lauterbur, et al. (2023)](https://doi.org/10.7554/eLife.84874) — Expanding the stdpopsim species catalog.

*"Es war einmal ..."*
