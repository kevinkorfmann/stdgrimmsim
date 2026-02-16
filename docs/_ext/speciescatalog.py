"""
Sphinx extension that provides the ``speciescatalog`` directive.

Usage in rst::

    .. speciescatalog:: ZweBerg

This auto-generates documentation for the given species, including genome
assembly info, chromosomes, and all demographic models.
"""

import stdgrimmsim
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from sphinx.util.nodes import nested_parse_with_titles


def _make_field_list(items):
    """Return rst lines for a field list."""
    lines = []
    for name, value in items:
        lines.append(f":{name}: {value}")
    return lines


def _format_rate(rate):
    """Format a scientific-notation rate nicely."""
    return f"{rate:.2e}"


def _build_species_rst(species_id):
    """Build rst content for a species."""
    species = stdgrimmsim.get_species(species_id)
    genome = species.genome

    lines = []

    # --- Genome summary ---
    lines.append(".. rubric:: Genome summary")
    lines.append("")
    items = [
        ("ID", f"``{species.id}``"),
        ("Species", f"*{species.name}*"),
        ("Common name", species.common_name),
        ("Assembly", f"``{genome.assembly_name}`` ({genome.assembly_accession})"),
        ("Ploidy", str(species.ploidy)),
        ("Generation time", f"{species.generation_time} years"),
        ("Population size", f"{species.population_size:,}"),
    ]
    lines.extend(_make_field_list(items))
    lines.append("")

    # --- Chromosomes table ---
    lines.append(".. rubric:: Chromosomes")
    lines.append("")
    lines.append(".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append("   :widths: 20 20 20 20")
    lines.append("")
    lines.append("   * - Name")
    lines.append("     - Length (bp)")
    lines.append("     - Mutation rate")
    lines.append("     - Recombination rate")

    for chrom in genome.chromosomes:
        lines.append(f"   * - {chrom.id}")
        lines.append(f"     - {chrom.length:,}")
        lines.append(f"     - {_format_rate(chrom.mutation_rate)}")
        lines.append(f"     - {_format_rate(chrom.recombination_rate)}")
    lines.append("")

    # --- Demographic models ---
    lines.append(".. rubric:: Demographic models")
    lines.append("")

    for model in species.demographic_models:
        lines.append(f"**{model.id}** — {model.description}")
        lines.append("")
        # Population list
        pop_names = ", ".join(
            f"``{p.name}``" for p in model.populations
        )
        lines.append(f"Populations: {pop_names}")
        lines.append("")
        if model.long_description and model.long_description.strip():
            for desc_line in model.long_description.strip().splitlines():
                lines.append(desc_line.strip())
            lines.append("")

    return lines


class SpeciesCatalogDirective(Directive):
    """Directive to render species catalog documentation."""

    required_arguments = 1  # species ID
    optional_arguments = 0
    has_content = False

    def run(self):
        species_id = self.arguments[0]
        try:
            rst_lines = _build_species_rst(species_id)
        except ValueError as e:
            error = self.state_machine.reporter.error(
                f"speciescatalog: {e}",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno,
            )
            return [error]

        # Parse the generated rst into docutils nodes
        rst_text = "\n".join(rst_lines)
        string_list = StringList(rst_lines, source="speciescatalog")
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, string_list, node)
        return node.children


def setup(app):
    app.add_directive("speciescatalog", SpeciesCatalogDirective)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
