stdvoidsim – install and use (hidden test dir)

Install (from repo root):
  pip install -e .

  Or use the script (creates .test/venv and installs there):
  .test/install_and_run.sh

Use (Python):
  import stdvoidsim
  species = stdvoidsim.get_species("DagHyd")   # Deep Ones
  model = species.get_demographic_model("InnsmouthDecline_1M27")
  contig = species.get_contig(length=10_000)
  engine = stdvoidsim.get_default_engine()
  ts = engine.simulate(model, contig, {"DeepOnes": 4})
  print(ts.num_trees, ts.num_sites)

Use (CLI):
  stdvoidsim DagHyd -d InnsmouthDecline_1M27 -L 10000 -o out.trees DeepOnes:4

Run the test script (from repo root, after install):
  python .test/run_simulation.py
  # or: .test/install_and_run.sh

Run SLiM engine test (script generation + optional run; diploid species only):
  python .test/run_slim_test.py
  # Script generation works without SLiM. Actual run requires SLiM on PATH (SLiM 3.x recommended; 4.x may need engine updates).
