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

project = "gtrending"
copyright = "2020-2022 hedy"
author = "hedy"

# The full version, including alpha/beta/rc tags
from gtrending import __version__

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

import sphinx_rtd_theme


# Register the theme as an extension to generate a sitemap.xml
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
