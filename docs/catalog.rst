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

**Heinzelmaennchen** (*Heinzelmaennchen coloniensis*) — The helpful elves of Cologne
who secretly did the townspeople's work at night, until a tailor's wife spied on them (Kopisch 1836).

.. speciescatalog:: HeiCol

**Kobold** (*Koboldus domesticus*) — House spirits bound to hearth and home,
ranging from helpful household helpers to mischievous mine spirits (Berggeist).

.. speciescatalog:: KobHau


.. _water-river-spirits:

Water & river spirits
=====================

**Nix** (*Nixus rhenanus*) — Water spirits from Rhine and Elbe folklore (Nix, Nixe).

.. speciescatalog:: NixRhe

**Loreley** (*Loreley rhenanus*) — The spirit of the Loreley rock on the Rhine (Brentano, Heine).

.. speciescatalog:: LorRhe

**Flussfee** (*Flussfee aquaticus*) — River fairies of the Rhine tributaries
(Main, Moselle, Neckar), linked to regional German river folklore.

.. speciescatalog:: FeeFlu


.. _forest-spirits:

Forest & nocturnal spirits
==========================

**Erlkoenig** (*Erlkoenig sylvestris*) — The Alder King of Goethe's ballad
and Herder's Danish Ellerkonge translation, haunting forest paths at dusk.

.. speciescatalog:: ErlKoe

**Alp** (*Alpus nocturnalis*) — The nightmare spirit (Alpdruck) that sits
on sleepers' chests, widespread in German and Alpine folklore.

.. speciescatalog:: AlpNac

**Wilde Jagd** (*Wildjaeger germanicus*) — The Wild Hunt, a spectral
host of riders that sweeps across the night sky (Grimm, *Deutsche Mythologie*).

.. speciescatalog:: WilJae


.. _mountain-regional-mythology:

Mountain & regional mythology
=============================

**Rübezahl** (*Ruebezahl harzensis*) — Mountain spirit (Berggeist) of the Riesengebirge (Krkonoše) and Harz.

.. speciescatalog:: RueHar

**Black Forest spirit** (*Silvani schwarzwaldensis*) — Forest spirits of the Schwarzwald.

.. speciescatalog:: SchWar


.. _shape-shifters-beasts:

Shape-shifters & mythical beasts
================================

**Werwolf** (*Werwolfus lupinus*) — Werewolves from German trial records
and folklore, particularly the Rhineland, Bavaria, and Livonian traditions.

.. speciescatalog:: WerWol

**Lindwurm** (*Lindwurm draconicus*) — The wingless dragon of Germanic
legend (Nibelungenlied's Fafnir, Klagenfurt Lindwurm), with long generation
times and small populations driven near extinction by hero-slaying.

.. speciescatalog:: LinDra


.. _generic-models:

Generic models
==============

In addition to the species-specific models listed in this catalog, ``stdgrimmsim`` offers
generic demographic models that can be run with any species.
These are described in the :ref:`API <sec_api_generic_models>`.

 - :meth:`stdgrimmsim.PiecewiseConstantSize`
 - :meth:`stdgrimmsim.IsolationWithMigration`
