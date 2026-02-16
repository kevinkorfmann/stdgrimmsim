.. stdgrimmsim documentation index file

Welcome to stdgrimmsim
====================

**Population genetic simulations for German folklore and mythology.**

``stdgrimmsim`` is a library of demographic and genome models for beings from
German folklore, fairy tales (Grimm), and regional mythology. Simulate dwarves,
water spirits (Nix), Rübezahl, Frau Holle, the Loreley, and Black Forest spirits
with made-up but population-genetically plausible parameters — powered by
`msprime <https://tskit.dev/msprime/>`_ and `SLiM <https://messerlab.org/slim/>`_
and built on the `stdpopsim <https://stdpopsim.readthedocs.io/>`_ framework.

.. epigraph::
   Es war einmal …
   — *Grimms' Fairy Tales*

First steps
-----------

- **Install:** :ref:`Installation <sec_installation>` — get ``stdgrimmsim`` on your machine.
- **Explore:** :ref:`Catalog <sec_catalog>` — 32 species and 150 demographic models.
- **Run:** :ref:`Tutorial <sec_tutorial>` — examples and workflows.

.. admonition:: Quick run
   :class: quick-run

   Install and simulate 10 mountain dwarf samples over 100 kb:

   .. code-block:: console

      $ pip install stdgrimmsim
      $ stdgrimmsim ZweBerg -d BlackForest_1D12 -o dwarves.trees -L 100000 BlackForest:10

   Then open ``dwarves.trees`` in `tskit <https://tskit.dev/tskit/>`_ or
   :ref:`continue with the tutorial <sec_tutorial>`.

Catalog at a glance
-------------------

The full :doc:`catalog <catalog>` lists every species and demographic model.
By category:

.. container:: catalog-at-a-glance

   - :ref:`Fairy tale & Grimm <fairy-tale-grimm>`
     - *Zwergus bergensis* (mountain dwarf), *Holle hesseensis* (Frau Holle)
   - :ref:`Water & river spirits <water-river-spirits>`
     - *Nixus rhenanus* (Nix), *Loreley rhenanus* (Loreley)
   - :ref:`Mountain & regional mythology <mountain-regional-mythology>`
     - *Ruebezahl harzensis* (Rübezahl), *Silvani schwarzwaldensis* (Black Forest spirit)
   - :ref:`Generic models <generic-models>`
     - Generic demographic models (any species)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   installation
   catalog
   all_models
   tutorial
   cli_arguments
   api
   development
   changelogs

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
