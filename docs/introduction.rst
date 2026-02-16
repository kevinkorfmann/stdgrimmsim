.. _sec_introduction:

============
Introduction
============

This is the documentation for ``stdgrimmsim``, a library of population
genetic simulation models for German folklore, fairy tales, and mythology.

``stdgrimmsim`` is a fork of ``stdvoidsim``/``stdpopsim`` that provides
6 species from German-speaking folklore: dwarves (Zwerge), water spirits (Nix),
mountain spirits (Rübezahl), Frau Holle, the Loreley, and Black Forest spirits.
Each species has made-up but population-genetically plausible genomes and
demographic models tied to geographic regions (Rhine, Harz, Schwarzwald, etc.).

Under the hood, ``stdgrimmsim`` relies on
`msprime <https://tskit.dev/software/msprime.html>`_ and
`SLiM 4 <https://messerlab.org/slim/>`_ to generate sample datasets in the
`tree sequence <https://tskit.dev/learn/>`_ format.


First steps
-----------

 - Head to the :ref:`Installation <sec_installation>` page to get ``stdgrimmsim`` installed
   on your computer.

 - Skim the :ref:`Catalog <sec_catalog>` to see what folklore simulations are currently
   supported by ``stdgrimmsim``.

 - Read the :ref:`Tutorials <sec_tutorial>` to see some examples of ``stdgrimmsim`` in
   action.


Citations
---------

``stdgrimmsim`` is built on the ``stdpopsim`` framework. If you use the simulation
framework, please cite:

  - Jeffrey R Adrion et al. (2020),
    *A community-maintained standard library of population genetic models*,
    eLife 9:e54967; doi: https://doi.org/10.7554/eLife.54967

  - M Elise Lauterbur et al. (2023),
    *Expanding the stdgrimmsim species catalog, and lessons learned for realistic genome simulations*,
    eLife 12:RP84874; doi: https://doi.org/10.7554/eLife.84874


Licence and usage
-----------------

``stdgrimmsim`` is available under the GPLv3 public license.
The terms of this license can be read
`here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_.
