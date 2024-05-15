# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Diario'
copyright = '2024, João Pedro Lacerda Sousa'
author = 'João Pedro Lacerda Sousa'
release = '15/05/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

# Adiciona o diretório do projeto ao sys.path
sys.path.insert(0, os.path.abspath('../'))

# Configura as variáveis de ambiente do Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'diario.settings'

import django
django.setup() # Substitua 'diario' pelo nome do diretório que contém settings.py

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]


templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
