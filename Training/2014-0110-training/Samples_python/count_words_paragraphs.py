#!/usr/bin/env python

import re

#
# "Duck typing" -- From Wikipedia, the free encyclopedia
#
Content_text = """\
In computer programming with object-oriented programming languages, duck typing
is a style of typing in which an object's methods and properties determine the
valid semantics, rather than its inheritance from a particular class or
implementation of a specific interface. The name of the concept refers to the
duck test, attributed to James Whitcomb Riley (see history below), which may be
phrased as follows: When I see a bird that walks like a duck and swims like a
duck and quacks like a duck, I call that bird a duck.

In duck typing, one is concerned with just those aspects of an object that are
used, rather than with the type of the object itself. For example, in a
non-duck-typed language, one can create a function that takes an object of type
Duck and calls that object's walk and quack methods. In a duck-typed language,
the equivalent function would take an object of any type and call that object's
walk and quack methods. If the object does not have the methods that are called
then the function signals a run-time error. If the object does have the
methods, then they are executed no matter the type of the object, evoking the
quotation and hence the name of this form of typing.

Duck typing is aided by habitually not testing for the type of arguments in
method and function bodies, relying on documentation, clear code and testing to
ensure correct use.
"""

Content_list = [
    "In computer programming with object-oriented programming languages,",
    "duck typing is a style of typing in which an object's methods and",
    "properties determine the valid semantics, rather than its",
    "inheritance from a particular class or implementation of a specific",
    "interface. The name of the concept refers to the duck test,",
    "attributed to James Whitcomb Riley (see history below), which may be",
    "phrased as follows: When I see a bird that walks like a duck and",
    "swims like a duck and quacks like a duck, I call that bird a duck.",
    "",
    "In duck typing, one is concerned with just those aspects of an",
    "object that are used, rather than with the type of the object",
    "itself. For example, in a non-duck-typed language, one can create a",
    "function that takes an object of type Duck and calls that object's",
    "walk and quack methods. In a duck-typed language, the equivalent",
    "function would take an object of any type and call that object's",
    "walk and quack methods. If the object does not have the methods that",
    "are called then the function signals a run-time error. If the object",
    "does have the methods, then they are executed no matter the type of",
    "the object, evoking the quotation and hence the name of this form of",
    "typing.",
    "",
    "Duck typing is aided by habitually not testing for the type of",
    "arguments in method and function bodies, relying on documentation,",
    "clear code and testing to ensure correct use.",
    "",
]


def count_words(content, transform_word):
    """Accumulate word counts for each word in a sequence of paragraphs.
    Print separate counts for each paragraph and total counts.
    """
    total_count = {}
    paragraph_count = {}
    index = 0
    content = content.splitlines()
    for line in content:
        line = line.strip()
        if not line:
            # We are at the end of a paragraph.  Print subtotals.
            index += 1
            msg = "Paragraph word count (%d):" % index
            print_totals(paragraph_count, msg)
            merge_counts(total_count, paragraph_count)
            paragraph_count = {}
        else:
            #words = line.split()
            words = re.split(r'\W+', line)
            for word in words:
                word = transform_word(word)
                paragraph_count.setdefault(word, 0)
                paragraph_count[word] += 1
    if paragraph_count:
        index += 1
        msg = "Paragraph word count (%d):" % index
        print_totals(paragraph_count, msg)
        merge_counts(total_count, paragraph_count)
    print_totals(total_count, "Total word count:")


def transform_word_lower(word):
    return word.lower()


def merge_counts(total_count, paragraph_count):
    """Merge (add) the word counts in one dictionary to another dictionary."""
    for word in paragraph_count:
        if word in total_count:
            total_count[word] += paragraph_count[word]
        else:
            total_count[word] = paragraph_count[word]


def print_totals(count, msg):
    """Print a header line and also the count for each word in a dictionary."""
    words = count.keys()
    words.sort()
    print '-' * 60
    print msg
    print '-' * 60
    for word in words:
        print '"%s": %d' % (word, count[word], )


def test():
    count_words(Content_text, transform_word_lower)


if __name__ == '__main__':
    #import ipdb; ipdb.set_trace()
    test()
