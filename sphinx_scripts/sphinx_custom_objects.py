def iter_replace(input_string, replacement_dict):
    '''Performs a regex replace

    Performs all regex replacements found in ``replacement_dict`` on
    ``input_string``.  The keys in ``replacement_dict`` are the search regexes
    and the values are the replacement values.

    Args:
        input_string (str) : The text to perform the replacement function on

        replacement_dict (dict) : A ``dict`` containing the keys (search
                    expressions) and values (replacement text).

    Returns:
        str : The ``input_string`` with the replacement defined in
                    ``replacement_dict``.
    '''
    rep = dict((re.escape(k), v) for k, v in replacement_dict.items())
    pattern = re.compile('|'.join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], input_string)

def escape_latex(text):
    '''escapes special characters in LaTeX

    Args:
        text (str) : The text to escape

    Returns:
        str: The escaped text
    '''
    replacements = {'&': r'\&',
                    '\\': r'\textbackslash',
                    '\n': r'\\',
                    '%': r'\%',
                    '$': r'\$',
                    '#': r'\#',
                    '_': r'\_',
                    '{': r'\{',
                    '}': r'\}',
                    '~': r'\textasciitilde',
                    '^': r'\textasciicircum',
                   }
    return iter_replace(str(text), replacements)

def wrap_table_cell(text, align='tl'):
    '''escapes and wraps data to be in a compatible format for LaTex

    The specified alignment only occurs if the text contains newlines ('\n').
    Multiline text is wrapped with ``\makecell`` and escaped.  If only a single
    line is passed, then it just escaped.

    Args:
        text (str) : A str with the cell contents

        align (str): A str containing the alignment requirements for the cell.
                     All values are option, defaults to 'tl'
                     Vertical alignment options are:
                        * ``t`` for top
                        * ``m`` for middle
                        * ``b`` for bottom
                     Horizontal alignment options are:
                        * ``l`` for left
                        * ``c`` for center
                        * ``r`` for right

    Returns:
        str : The wrapped cell contents properly escaped.
    '''
    # Handle None from yaml
    if text is None:
        return ''
    wrap_cell = False
    if '\n' in str(text):
        wrap_cell = True
    text = escape_latex(text)
    if wrap_cell:
        return ''.join(['\makecell[', align, ']{', text, '}'])
    return text

def array_to_latex_table(rows, header=False, grid=False):
    '''creates a LaTeX table from list or a list of lists

    This creates the "guts" of a LaTeX table from a list (single row) or a list
    of lists (table).  This DOES NOT create any ``table`` environments, captions,
    or anything else, this just takes the information in the lists and creates
    a ``str`` to represent the cells.

    Args:
        rows (list) : A ``list`` or ``list`` of ``lists``.  Each item is the
                      contents of a single table cell.

        header (bool) : If ``True``, it will make the cell contents bold.

        grid (bool) : If ``True`` it will append a horizontal line after each
                      row.

    Returns:
        str : A string with valid LaTeX table contents (no table env).
    '''
    latex_row = ''
    latex_rows = []
    if rows:
        if not isinstance(rows[0], list):
            rows = [rows]
    for row in rows:
        try:
            if header:
                latex_row = ' & '.join([''.join(['\\makecell{\\textbf{', escape_latex(col), '}}']) for col in row])
            else:
                latex_row = ' & '.join([wrap_table_cell(col) for col in row])
            if grid:
                latex_row = ' & '.join([''.join(['', col, '']) for col in row])
            else:
                latex_row = ' '.join([latex_row, r' \\'])
        except:
            print ('\nproblematic row: \n{}\n'.format(row))
            raise
        latex_rows = latex_rows + [latex_row]
    return '\n'.join(latex_rows)
