# Configuration file for the Sphinx documentation builder.

import sys, os

# -- Project information

project = "resource-namer"
copyright = "2022, Daren Race"
author = "Daren Race"

sys.path.insert(0, os.path.abspath("../../../resource-namer"))

# sys.path.insert(0, os.path.abspath(".."))

import resource_namer


release = version = resource_namer.__meta__.__version__

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "logo_only": True,
    # Toc options
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
    "display_version": True,
}

# -- Options for EPUB output
epub_show_urls = "footnote"
