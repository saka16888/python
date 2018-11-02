"""
Sample Python code to illustrate lexical features of Python.

Lexical features:

- Comments
- Name characters - alpha + digits + underscore.  First char not digit.
- Case significant
- Names have scope; single namespace within a given scope.
- A name can be of any length.
- Keywords
- Operators
- Line structure, line and statement ending, statement continuation,
  statement separator (;)
- Statement structure
- Blocks and indentation
- Special names


Keywords:

    and       del       from      not       while
    as        elif      global    or        with
    assert    else      if        pass      yield
    break     except    import    print
    class     exec      in        raise
    continue  finally   is        return
    def       for       lambda    try


Operators:

    +       -       *       **      /       //      %
    <<      >>      &       |       ^       ~
    <       >       <=      >=      ==      !=      <>

    and     or      is      not     in

    Also:   ()      []      . (dot)


Special names:

- __XXX__ -- Names with beginning and ending double underscores.
- _XXX or XXX_ -- Names that begin with a single underscore
  indicate (hint) "private" or "hidden" or internal use.  A trailing
  underscore may be used to avoid conflicts with keywords.
  (See "Naming conventions" in "Style Guide for Python Code":
  http://www.python.org/dev/peps/pep-0008/)
- int, float, str, list, tuple, dict, file, bool, ... -- Names of built-in
  classes/types.
- True, False, None, ... -- A few unique objects.
- Built-ins -- See http://docs.python.org/lib/builtin.html and
  http://docs.python.org/lib/built-in-funcs.html.


Line structure:

- Normally, one statement per line.
- The statement separator (semicolon) separates two statements on same line.
- The continuation character (backslash) is used to continue a statement
  on a subsequent line.
- In an open context, a continuation character is not needed.  An open
  context is parens, square brackets, and curley brackets.


Statement structure:

- Compound statements have a header and a body/block.
- Header starts with a keyword (for example, "for", "if", "def", "class")
  and ends with a colon (":").
- Header is followed by an indented block.
- Some compound statements have additional clauses, for example:
  - "try: except: ..."
  - "if: elif: ... else:"

Blocks and indentation:

- Indent starts a block.
- Out-dent ends a block.
- Empty block -- pass.
- Always use 4 spaces and no hard tabs for indentation.


Naming conventions:

- Globals -- all upper case.
- Modules -- all lower case.
- Functions and methods -- lower case with underscores.
- Local variables -- lower case.
- Class names -- Bumpy caps with initial cap.


Modules:

- A module can be imported (by other modules).
- A module can be run.
- A module is a file containing Python source code with extension ".py".


Module organization:

1. Module doc string
2. Imports
3. Globals
4. Function definitions for external use
5. Class definitions
6. Function definitions for internal use
7. Test harness or code that runs the script.
8. if __name__ == "__main__":


Style Guide for Python Code -- http://www.python.org/dev/peps/pep-0008


"""


#
# Imports

import sys


#
# Globals

VERSION = "Lexical samples version 1.0"

GLOBAL1 = """Here is a
triple quoted
string.
It contains new-line characters.
"""

GLOBAL2 = """Here is a another
triple quoted
string.
It contains new-line characters.
And, this one is surrounded by triple single-quotes.
We can put both 'single' and "double" quotes inside it.
"""


def make_node():
    node = TreeNode()        # Create an instance of class TreeNode.
    return node


class TreeNode(object):
    pass


def indent_sample(key, items):
    if key == 'active':
        key = 'inactive'
        print 'deactivated'
        for index, item in enumerate(items):
            print index
            print item
        for item in items:
            print 'before deactivating item:', item
            deactivate(item)
            print 'after deactivating item:', item
    else:
        key = 'active'
        print 'activated'
        for item in items:
            print 'before activating item:', item
            activate(item)
            print 'after activating item:', item


def activate(item):
    pass


def deactivate(item):
    pass


def test(command):
    long_parameter_name_one = 1
    long_parameter_name_two = 2
    long_parameter_name_three = 3
    long_parameter_name_four = 4
    result = None
    if command == 'calc':

        value1 = long_parameter_name_one + long_parameter_name_two + \
            long_parameter_name_three + long_parameter_name_four

        value2 = (long_parameter_name_one + long_parameter_name_two +
                  long_parameter_name_three + long_parameter_name_four)

        result = test_one(
            long_parameter_name_one, long_parameter_name_two,
            long_parameter_name_three, long_parameter_name_four)

        print result
        if long_parameter_name_one < 0 and \
                long_parameter_name_two < 0 and \
                long_parameter_name_three < 0 and \
                long_parameter_name_four:
            print 'Great'
        elif (long_parameter_name_one > 0 or
                long_parameter_name_two > 0 or
                long_parameter_name_three > 0 or
                long_parameter_name_four > 0):
            print 'Fine'
            print 'Real fine'
        else:
            print 'OK'
            print 'Okie Dokie'
        print value1, value2
    if command == 'ok':
        print 'ok'
    elif command == 'calc':
        print 'calc'
    elif command == 'close':
        print 'close'
    else:
        print 'other'
    str1 = "Strings can be single quoted" + ' or double-quoted.'
    print str1
    return result


def test_one(p1, p2, p3, p4):
    return p1, p2, p3, p4


def usage():
    print 'Usage ...'
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 3:
        usage()
    command = args[0]
    arg1 = args[1]
    arg2 = args[2]
    print arg1, arg2
    if command == 'show' or \
            command == 'calc' or \
            command == 'recalc' or \
            command == 'execute':
        test(command)
    if (command == 'show' or
            command == 'calc' or
            command == 'recalc' or
            command == 'execute'):
        test(command)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
