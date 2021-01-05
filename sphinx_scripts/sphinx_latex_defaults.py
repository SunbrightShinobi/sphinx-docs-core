# -- Options for LaTeX output ---------------------------------------------
# The master toctree document.
master_doc = 'index'

#latex_engine = 'lualatex'

PREAMBLE = string.Template(open(r'./common/_templates/preamble.tex').read())

latex_docclass = {
    'howto': 'article',
    'manual': 'report',
}

latex_contents = r'''
    \setupHeadFootForFrontMatter
    \formattoc
    \maketitle
    \pdfbookmark{APPROVAL SHEET}{sigpage}
    \signaturepage
    \pdfbookmark{DOCUMENT CHANGE HISTORY}{revhistory}
    \revisionhistory
    \pagenumbering{roman}
    \setcounter{page}{1}
    \renewcommand{\custompagenumberformat}{%
      \thepage\\
    }
    \pdfbookmark{\contentsname}{toc}
    \tableofcontents
    % The PDF bookmarks require new pages it seems, since
    % the Triton format doesn't have new pages, the other
    % "LIST OF XXX" bookmarks don't work.
    \clearpage
    %\pdfbookmark{\listfigurename}{toc}
    \listoffigures
    \clearpage
    %\pdfbookmark{\listtablename}{toc}
    \listoftables
    \clearpage
    \setupHeadFootForText
    \pagenumbering{arabic}
    \pagestyle{plain}

'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    #'fontpkg': r'''
    #            %\usepackage{times}
    #            % \setmainfont{Times}
    #            %\setsansfont{helvetica}
    #            %\setmonofont{courier}
    #            ''',



    'sphinxsetup': 'hmargin={.5in,.5in}, vmargin={1.3in,1.1in}',

# Additional stuff for the LaTeX preamble.
    'preamble': PREAMBLE.substitute(address=address,
                                    classification=classification,
                                    docrevision=document_rev,
                                    documentnumber=documentnumber,
                                    revisionhistory=array_to_latex_table(yaml.load(open('Revision_History.yaml').read(), Loader=yaml.FullLoader), grid=True),
                                    cmversion=cmstatus,
                                    project=project,
                                    changeNotice=changeNotice,
                                    systemName=systemName,
                                    csci=csci,
                                    responsibleEngineer=responsibleEngineer,
                                    docReleaseDate=docReleaseDate,
                                    docReleaseDesc=docReleaseDesc,
                                    doc_sw_pn_current=doc_sw_pn_current,
                                    doc_sw_pn_dash_current=doc_sw_pn_dash_current,
                                    doc_sw_pn_previous=doc_sw_pn_previous,
                                    doc_sw_pn_dash_previous=doc_sw_pn_dash_previous,
                                    contractNum=contractNum,
                                    cdrlNum=cdrlNum,
                                   ),

    'tableofcontents': latex_contents,

    # Make this not look like a book
    'classoptions': ',openany,oneside',

    'babel': r'\usepackage[english]{babel}',

    #'latex_top_level_sectioning': 'part',
    #'fncychap': '',
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',

}

# print(latex_elements)
latex_top_level_sectioning= 'part'

latex_additional_files = ['./common/_templates/procedure.sty',
                          './common/_templates/titlelogo.png',
                          './common/_templates/sphinxmanual.cls',
                         ]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [(master_doc,
                    file_name+'.tex',
                    project,
                    author, 
                    'manual')]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = './common/logo.eps'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False


# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc,
              file_name,
              project,
              [author],
              1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(master_doc,
                      file_name,
                      project,
                      author,
                      file_name,
                      'One line description of project.',
                      'Miscellaneous')]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


