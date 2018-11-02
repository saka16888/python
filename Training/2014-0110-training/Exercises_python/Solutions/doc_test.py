
def convert_str(instr, mult):
    """
    >>> from doc_test import convert_str
    >>> convert_str('aabbcc', 3)
    'AABBCCAABBCCAABBCC'
    >>> convert_str('xyz', 4)
    'XYZXYZXYZXYZ'
    >>>
    """
    newstr = instr.upper() * (mult + 1)
    return newstr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
