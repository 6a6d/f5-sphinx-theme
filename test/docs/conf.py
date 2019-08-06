# -*- coding: utf-8 -*-
#
# testdocs documentation build configuration file, created by
# sphinx-quickstart on Thu Nov  9 03:15:40 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime
import string
import re
#import f5_sphinx_theme


start_year = '2017'
current_year = datetime.date.today().strftime('%Y')
if start_year == current_year:
    copyright_year = start_year
else:
    copyright_year = '%s-%s' % (start_year, current_year)


# def setup(app):
#     app.add_stylesheet('css/icontrollx.css')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinxjp.themes.basicstrap',
  'sphinx.ext.todo',
  'sphinx.ext.autosectionlabel',
  'sphinx.ext.intersphinx',
  'sphinx.ext.coverage',
  'sphinx.ext.ifconfig',
  'sphinx.ext.doctest',
  'cloud_sptheme.ext.table_styling',
  'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'markdown',
  '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'F5 Sphinx Theme Test/Dev Docs'
copyright = u'%s, F5 Networks' % copyright_year
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0.1'

# Enter substitutions for commonly-used URLs, words, or phrases below.
# Try to keep sorted alphabetically.
# Preface links to other sites in clouddocs.f5.com with '%(base_url)s'
# Example:
# .. _F5 Container Connectors: %(base_url)s/containers/latest

rst_epilog = """
.. |platform| replace:: Docker
"""
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    '_static/reuse',
    'drafts',
    'Thumbs.db',
    '.DS_Store',
    'venv',
    '.github'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_emit_warnings = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'f5_sphinx_theme'
html_theme_path = ['../../']
html_theme_options = {
    # 'site_name': project,
    'next_prev_link': True,
    'version_selector': True,
    'base_url': '/'
 }
html_sidebars = {['**': 'localtoc.html', 'globaltoc.html','relations.html']}

html_theme_options = {
  'version_selector': True,
}

html_context = {
    'version_meta_path': './versions.json',
    'project_safe': re.sub('[^A-Za-z0-9]+', '', project)
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
#
html_short_title = 'Home'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = ''

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
html_domain_indices = True

# If false, no index is generated.
#
html_use_index = True

# If true, the index is split into individual pages for each letter.
#
html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
#html_use_opensearch = 'http://clouddocs.f5.com'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'f5_theme_docs'

# -- Options for linkcheck ------------------------------------------------
# A list of regular expressions that match URIs that should not be checked when doing a linkcheck build. Example:
#linkcheck_ignore = [r'http://localhost:\d+/']

# The number of times the linkcheck builder will attempt to check a URL before declaring it broken. Defaults to 1 attempt.
linkcheck_retries = 2

# A timeout value, in seconds, for the linkcheck builder. The default is to use Python’s global socket timeout.
linkcheck_timeout = 5

linkcheck_anchors = False

# -- Options for LaTeX output ---------------------------------------------
#
# template = string.Template(open('preamble.tex').read())
#
# latex_contents = r"""
# \frontcoverpage
# \contentspage
# """
#
# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     'papersize': 'letterpaper',
#
#     # The font size ('10pt', '11pt' or '12pt').
#     #
#     'pointsize': '10pt',
#
#     # Additional stuff for the LaTeX preamble.
#     #
#     'preamble': template.substitute(
#                                     project=project,
#                                     author=author,
#                                     frontcoverimage='',
#                                     backcoverimage=''
#     ),
#     'tableofcontents': latex_contents,
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, '%s.tex' % cleanname, u'icontrol lxdocs' ,
#      u'F5 Networks, Inc.', 'manual', True),
# ]
#

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, 'testdocs', u'testdocs Documentation',
#      [author], 1)
# ]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'testdocs', u'testdocs Documentation',
#      author, 'testdocs', 'One line description of project.',
#      'Miscellaneous'),
# ]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
# epub_title = project
# epub_author = author
# epub_publisher = author
# epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
# epub_exclude_files = ['search.html']


