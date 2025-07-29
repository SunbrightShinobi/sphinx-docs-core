import re
import sphinx
import tablib
import ciscoconfparse
import os
from pathlib import Path


# Load the custom objects for sphinx
exec(open(r'./sphinx_scripts/sphinx_custom_objects.py').read())

# -- General configuration ------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_jinja',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.actdiag',
    'sphinx_git',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.jupyter',
    'sphinxcontrib.ansibleautodoc',
    'sphinxcontrib.confluencebuilder',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinxcontrib.drawio',
    'sphinxdrawio.drawio_html',
    'sphinxcontrib.bibtex',
]

# Configuration settings for imgmath
imgmath_image_format = "png"
# Configuration settings for seqdiag
seqdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
seqdiag_html_image_format = "SVG"
seqdiag_latex_image_format = "PDF"

# Configuration settings for nwdiag, rackdiag(nwdiag), packetdiag(nwdiag)
nwdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
nwdiag_html_image_format = "SVG"
nwdiag_latex_image_format = "PDF"
rackdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
rackdiag_html_image_format = "SVG"
rackdiag_latex_image_format = "PDF"
packetdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
packetdiag_html_image_format = "SVG"
packetdiag_latex_image_format = "PDF"

# Configuration settings for blockdiag
blockdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
blockdiag_html_image_format = "SVG"
blockdiag_latex_image_format = "PDF"

# Configuration settings for actdiag
actdiag_fontpath = '/usr/share/fonts/dejavu/DejaVuSans.ttf'
actdiag_html_image_format = "SVG"
actdiag_latex_image_format = "PDF"

# Configuration settings for plantuml
plantuml_output_format = "svg"
plantuml_latex_output_format = "pdf"

numfig = True
numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s',
                 'code-block': 'Code %s',
                 'section': 'Section %s',
                }

# Configuration settings for draw.io
#drawio_binary_path = 
drawio_headless = "auto"  #svg=False,png=True,pdf=unknown
drawio_builder_export_format = {"html": "svg", "latex": "pdf", "rinoh": "pdf"} #svg looks best
drawio_default_export_scale = 100
drawio_default_transparency = False
drawio_no_sandbox = False
drawio_disable_gpu = False
drawio_disable_verbose_electron = False
drawio_disable_dev_shm_usage = False

# bibtex configuration settings
bibtex_bibfiles = ['common_docs/references/refs.bib']
bibtex_default_style = 'alpha' #[alpha, plain, unsrt, usrtalpha]
bibtex_encoding = 'utf-8-sig' #[utf-8-sig,latin]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
todo_emit_warnings = True
todo_link_only = True

highlight_languange = 'shell-session'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Suppress known warnings
# Suppress autosectionlabel warnings when you have duplicate labels
suppress_warnings = ['autosectionlabel.*']
################################################################################
# Setup CM Status
################################################################################
# Load the git configuration
exec(open(r'./sphinx_scripts/sphinx_git.py').read())

cmstatus='Non-CM'
if is_in_git():
    cmstatus = get_git_status()
    gitstatus = 'inGit'


# set filename
file_name = '_'.join([documentnumber,
                      document_rev,
                      project.replace(' ', '_'),
                      csci.replace(' ', '_'),
                      release.replace('.', '_').replace(' ', '_'),])

rst_prolog = """
.. |project| replace:: {project}

.. |git_repo| replace:: {git_repo}

""".format(project=project,
           git_repo=git_repo,
           )

#Jinja Configuration
jinja_base = Path(".").resolve() # Allows Jinja to find configured templates not in default path

# Load the html configuration
exec(open(r'./sphinx_scripts/sphinx_html_defaults.py').read())
# Load the latexpdf configuration
exec(open(r'./sphinx_scripts/sphinx_latex_defaults.py').read())

