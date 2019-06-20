import re

with open('notes/team_history.txt') as f:
    hist = f.read()
print(hist,"\n")

# .
pattern=r'\|.'
ret=re.findall(pattern, hist)
print("pattern = %s , ret = %s" % (pattern,ret))

# ^
#(Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
pattern=r'^ON'
ret=re.findall(pattern, hist)
print("pattern = %s , ret = %s" % (pattern,ret))

pattern=r'\^ON'
ret=re.findall(pattern, hist)
print("pattern = %s , ret = %s" % (pattern,ret))

pattern=r'\*ON[\w]*'
ret=re.findall(pattern, hist)
print("pattern = %s , ret = %s" % (pattern,ret))

pattern=r'O.'
ret=re.findall(pattern, hist)
print("pattern = %r , ret = %r" % (pattern,ret))
pattern=r'.O.'
ret=re.findall(pattern, hist)
print("pattern = %r , ret = %r" % (pattern,ret))

# $


# *


# +


# ?


# *?, +?, ??


# {m}

# {m,n}


# {m,n}?

# \

# \number
# \A, \b, \B, \d, \D, \s, \S, \w, \W,
#\a      \b      \f      \n
#\r      \t      \u      \U
#\v      \x      \\

# [  |  ]

# (...)

# (?...)

# (?aiLmsux) (One or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x'.)
# The group matches the empty string; the letters set the corresponding flags:
# re.A (ASCII-only matching), re.I (ignore case),
# re.L (locale dependent),
# re.M (multi-line), re.S (dot matches all), re.U (Unicode matching), and re.X (verbose),
# for the entire regular expression. (The flags are described in Module Contents.)
# This is useful if you wish to include the flags as part of the regular expression,
# instead of passing a flag argument to the re.compile() function.
# Flags should be used first in the expression string.


