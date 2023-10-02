import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../.."))


project = "pymemuc"
copyright = "2023, Martin Miglio"  # noqa #pylint: disable=redefined-builtin
author = "Martin Miglio"

locale_dirs = ["locales/"]

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autodoc_default_options = {
    "member-order": "bysource",
}
add_module_names = False


html_theme = "furo"
html_theme_options = {
    "sidebarwidth": "19em",
}
htmlhelp_basename = "pymemuc"
intersphinx_mapping = {"Python Docs": ("http://docs.python.org/", None)}

html_js_files = [
    (
        "https://analytics.martinmiglio.dev/script.js",
        {"data-website-id": "28d008aa-35e3-4aaa-8964-b06ec824bfed", "async": "async"},
    ),
]
