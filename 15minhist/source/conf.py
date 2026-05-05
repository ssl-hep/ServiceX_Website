# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import urllib.error
import urllib.request

# Pull install/setup content from the ServiceX_frontend repo so it lives in one place.
_HERE = os.path.dirname(os.path.abspath(__file__))
_UPSTREAM_SETUP_URL = (
    "https://raw.githubusercontent.com/ssl-hep/ServiceX_frontend/"
    "master/docs/userguide/source/setup.md"
)
_INCLUDE_PATH = os.path.join(_HERE, "_includes", "setup.md")

os.makedirs(os.path.dirname(_INCLUDE_PATH), exist_ok=True)
try:
    urllib.request.urlretrieve(_UPSTREAM_SETUP_URL, _INCLUDE_PATH)
except urllib.error.URLError as exc:
    if not os.path.exists(_INCLUDE_PATH):
        raise RuntimeError(
            f"Failed to download {_UPSTREAM_SETUP_URL}: {exc}"
        ) from exc

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
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
    "code_include.extension",
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "enum_tools.autoenum",
]

myst_enable_extensions = [
    "colon_fence",
]

templates_path = ['_templates']

html_css_files = [
    ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css', {'crossorigin': 'anonymous'}),
    ('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css', {'crossorigin': 'anonymous'}),
    ('https://tryservicex.org/css/navbar.css', {'crossorigin': 'anonymous'}),
    ('https://tryservicex.org/css/sphinx.css', {'crossorigin': 'anonymous'}),
]

html_js_files = [
    ('https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js', 
        {'integrity': 'sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI', 'crossorigin': 'anonymous'}
    ),
]

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/scroll-start.html",
        "sidebar/scroll-end.html",
    ]
}

html_theme = "furo"