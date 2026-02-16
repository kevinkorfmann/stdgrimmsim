.. _sec_catalog:

=======
Catalog
=======

This catalog lists every species from German folklore and mythology available
for simulation in ``stdgrimmsim``. Each has made-up but population-genetically
plausible genomes and demographic histories tied to geographic regions (Black Forest,
Harz, Rhine, etc.) and to Grimm fairy tales where relevant.

1. Which **chromosome** (:class:`.Genome` object)?
2. Which **model of demographic history** (:class:`.DemographicModel` object)?

Example: simulate mountain dwarf samples under the Black Forest demographic model:

.. code-block:: console

    $ stdgrimmsim ZweBerg -d BlackForest_1D12 -o dwarves.trees -L 100000 BlackForest:10


.. _fairy-tale-grimm:

Fairy tale & Grimm
==================

.. _mountain-dwarves:

**Mountain Dwarves** (*Zwergus bergensis*) — Bergzwerge from Grimm and regional
folklore, associated with mines and forests (e.g. Snow White's dwarves, Harz and Schwarzwald).

.. speciescatalog:: ZweBerg

**Frau Holle** (*Holle hesseensis*) — The fairy-tale figure from Grimm KHM 24,
associated with the well, snow, and the realm beyond (Hesse/Thuringia).

.. speciescatalog:: FraHol


.. _water-river-spirits:

Water & river spirits
=====================

**Nix** (*Nixus rhenanus*) — Water spirits from Rhine and Elbe folklore (Nix, Nixe).

.. speciescatalog:: NixRhe

**Loreley** (*Loreley rhenanus*) — The spirit of the Loreley rock on the Rhine (Brentano, Heine).

.. speciescatalog:: LorRhe


.. _mountain-regional-mythology:

Mountain & regional mythology
=============================

**Rübezahl** (*Ruebezahl harzensis*) — Mountain spirit (Berggeist) of the Riesengebirge (Krkonoše) and Harz.

.. speciescatalog:: RueHar

**Black Forest spirit** (*Silvani schwarzwaldensis*) — Forest spirits of the Schwarzwald.

.. speciescatalog:: SchWar


.. _generic-models:

Generic models
==============

In addition to the species-specific models listed in this catalog, ``stdgrimmsim`` offers
generic demographic models that can be run with any species.
These are described in the :ref:`API <sec_api_generic_models>`.

 - :meth:`stdgrimmsim.PiecewiseConstantSize`
 - :meth:`stdgrimmsim.IsolationWithMigration`
