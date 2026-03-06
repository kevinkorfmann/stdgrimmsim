.. _sec_introduction:

============
Introduction
============

This is the documentation for ``stdgrimmsim``, a library of population
genetic simulation models for German folklore, fairy tales, and mythology.

Purpose
-------

``stdgrimmsim`` is a *fork catalog* of ``stdpopsim``: it shares the same API and
simulation engines but replaces the species catalog with 32 fictional taxa from
German-speaking folklore.

**Primary use case:** generating diverse, plausible training data for ML/DL-based
population-genetic inference methods and for systematic parameter-space benchmarking.

All species are diploid with demographically plausible parameters
(Ne from 2,000 to 420,000; generation times 8-200 years). Demographies are tied
to **geographic regions** (Black Forest, Harz, Rhine, Bavaria, Prussia, Saxony) and
**folkloric narratives** (Frau Holle's well, Rubezahl's mountain, the Loreley rock).

See also: `stdvoidsim <https://github.com/kevinkorfmann/stdvoidsim>`_ - the
companion catalog for stress-testing with extreme Lovecraftian scenarios
(40 species, 80 models; Ne from 1 to 10^6, generation times 0.01-10^6 years).


Model complexity taxonomy
-------------------------

Models in ``stdgrimmsim`` are organized by population count into four levels:

- **Level 1** - 1-population constant or piecewise-constant (68 models).
  Simplest baseline for any species.
  Examples: ``BlackForest_1D12``, ``WellRealm_1D12``, ``Rhine_1D12``.

- **Level 2** - 2-population split +/- migration (48 models).
  Two populations diverging from an ancestor.
  Examples: ``HarzBlackForest_2D12``, ``RhineElbe_2D12``, ``WellSnow_2D12``.

- **Level 3** - 3-population (20 models).
  Examples: ``ThreeRivers_3D12``, ``ThreeForestRealms_3D12``.

- **Level 4** - 4-population (14 models).
  Examples: ``FourMountainRanges_4D12``, ``FourRealms_4D12``.

This structured progression allows users to sweep over complexity levels
systematically (e.g., evaluate on all Level-1 models, then test generalisation
to 2-, 3-, and 4-population histories).


Species categories
------------------

The 32 species are grouped into thematic categories:

- **Fairy-tale & Grimm:** Mountain Dwarves (ZweBerg), Frau Holle (FraHol),
  Heinzelmannchen (HeiCol), Kobold (KobHau), Rumpelstiltskin (RumSti),
  Seven Ravens (SieRab), Cinderella doves (AscPut), Town Musicians (BreSta).

- **Water & river spirits:** Nix (NixRhe), Loreley (LorRhe), River Fairy (FeeFlu).

- **Forest & nocturnal spirits:** Erlkoenig (ErlKoe), Alp (AlpNac),
  Wild Hunt (WilJae), Mill Ghost (MueGei).

- **Mountain & regional mythology:** Rubezahl (RueHar), Black Forest spirit
  (SchWar), Erzgebirge spirit (SaxErz).

- **Regional:** Bavaria (WolBay, BerAlp, MooBay), Prussia (PukPru, OstBal,
  MasLak), Pomerania (PomBal).

- **Shape-shifters & mythical beasts:** Werewolf (WerWol), Lindwurm (LinDra),
  Firedrake (DraFeu), Basilisk (BasRex).

- **Pre-Christian & Germanic:** Frost Giant (JotRie), Valkyrie (ValKri).

- **17th-18th century:** Walpurgis Witch (HexWal).


First steps
-----------

 - Head to the :ref:`Installation <sec_installation>` page to get ``stdgrimmsim``
   installed on your computer.

 - Skim the :ref:`Catalog <sec_catalog>` to see all 32 species and 150 demographic
   models.

 - Read the :ref:`Tutorials <sec_tutorial>` to see some examples of ``stdgrimmsim``
   in action.


Citations
---------

``stdgrimmsim`` is built on the ``stdpopsim`` framework. If you use the simulation
framework, please cite:

  - Jeffrey R Adrion et al. (2020),
    *A community-maintained standard library of population genetic models*,
    eLife 9:e54967; doi: https://doi.org/10.7554/eLife.54967

  - M Elise Lauterbur et al. (2023),
    *Expanding the stdpopsim species catalog, and lessons learned for realistic genome simulations*,
    eLife 12:RP84874; doi: https://doi.org/10.7554/eLife.84874


Licence and usage
-----------------

``stdgrimmsim`` is available under the GPLv3 public license.
The terms of this license can be read
`here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.
