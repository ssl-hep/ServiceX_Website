# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The 15 Minute Histogram Challenge'
copyright = (
    "2026 Institute for Research and " "Innovation in Software for High Energy Physics (IRIS-HEP)"
)
author = "Institute for Research and Innovation in Software for High Energy Physics (IRIS-HEP)"
release = "0.1.0"
html_title = "The 15 Minute Histogram Challenge"
html_short_title = "15min Histogram"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]


exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
