"""
usage: python files1.py <inputfilename>

"""

import sys
import os
import re


Content = [
    '"Promised Land", by Chuck Berry',
    '',
    "I left my home in norfolk virginia,",
    "California on my mind.",
    "Straddled that greyhound, rode him past raleigh,",
    "On across caroline.",
    "",
    "Stopped in charlotte and bypassed rock hill,",
    "And we never was a minute late.",
    "We was ninety miles out of atlanta by sundown,",
    "Rollin' 'cross the georgia state.",
    "",
    "We had motor trouble it turned into a struggle,",
    "Half way 'cross alabam,",
    "And that 'hound broke down and left us all stranded",
    "In downtown birmingham.",
    "",
    "Straight off, I bought me a through train ticket,",
    "Ridin' cross mississippi clean",
    "And I was on that midnight flyer out of birmingham",
    "Smoking into new orleans.",
    "",
    "Somebody help me get out of louisiana",
    "Just help me get to houston town.",
    "There's people there who care a little 'bout me",
    "And they won't let the poor boy down.",
    "",
    "Sure as you're born, they bought me a silk suit,",
    "Put luggage in my hands,",
    "And I woke up high over albuquerque",
    "On a jet to the promised land.",
    "",
    "Workin' on a t-bone steak a la carte",
    "Flying over to the golden state;",
    "The pilot told me in thirteen minutes",
    "We'd be headin' in the terminal gate.",
    "",
    "Swing low sweet chariot, come down easy",
    "Taxi to the terminal zone;",
    "Cut your engines, cool your wings,",
    "And let me make it to the telephone.",
    "",
    "Los angeles give me norfolk virginia,",
    "Tidewater four ten o nine",
    "Tell the folks back home this is the promised land callin'",
    "And the poor boy's on the line",
]


def print_lines(filename):
    """Print all the lines in a file.
    """
    infile = open(filename, 'r')
    for line in infile:
        print 'Line: %s' % (line.rstrip(), )
    infile.close()


def print_lines_2(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            print 'line:', line,
    print
    print infile
    print


def print_lines_3(filename, transform):
    """Print all the lines in a file.
    """
    infile = open(filename, 'r')
    for line in infile:
        line = line.rstrip()
        line = transform(line)
        print 'Line: %s' % (line, )
    infile.close()


def transform1(line):
    return line.upper()


def count_words(filename):
    """Count the total number of words in a file.
    """
    infile = open(filename, 'r')
    count = 0
    lines = infile.readlines()
    for line in lines:
        # words = line.split()
        words = re.split('\W+', line)
        count1 = len(words)
        count += count1
        #sys.stdout.write('%d: %s' % (count1, line, ))
    infile.close()
    print 'count: %d' % count
    return count


def write_file(filename, content):
    """Write each of the strings in an array of strings to a file.
    """
    outfile = open(filename, 'w')
    for line in content:
        outfile.write('%s\n' % line)
    outfile.close()


def test(infilename):
    """Run our tests.
    """
    #print_lines(infilename)
    print_lines_2(infilename)
    print_lines_3(infilename, transform1)
    count = count_words(infilename)
    print 'returned count: %d' % count
    if os.path.exists('tmp.txt'):
        sys.stderr.write('tmp.txt exists.  remove it.\n')
        sys.exit(1)
    write_file('tmp.txt', Content)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        sys.stderr.write(__doc__)
        sys.exit(1)
    infilename = args[0]
    test(infilename)


if __name__ == '__main__':
    main()
