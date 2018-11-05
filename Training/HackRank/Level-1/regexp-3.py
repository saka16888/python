'''
Python offers two different primitive operations based on regular expressions:
match checks for a match only at the beginning of the string,
while search checks for a match anywhere
in the string (this is what Perl does by default).
'''
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

searchObj = re.search( r'smarter than dogs', line, re.M|re.I)
if searchObj:
   print("search --> searchObj.group() : ", searchObj.group())
else:
   print("Nothing found!!")