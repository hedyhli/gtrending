# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------
from gtrending import __version__, __url__, __author__

project = "gtrending"
author = __author__
copyright = "2020-2023 " + author

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"

# --- theme ---

# Register the theme as an extension to generate a sitemap.xml
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx_copybutton",
]
doctest_global_setup = "from gtrending import *"

html_theme = "furo"
# "edit" button
html_theme_options = {
    "source_repository": "https://github.com/hedyhli/gtrending",
    "source_branch": "master",
    "source_directory": "docs/",
}
html_show_search_summary = True
html_title = f"{project} {release}"

# copy button
# don't copy the python REPL and terminal shell prompt
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
