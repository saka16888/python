.. vim: set ft=rst:

===========================
Python Training Materials
===========================

:author: Dave Kuhlman
:contact: dkuhlman@davekuhlman.org
:address:
    http://www.davekuhlman.org

:revision: 1.0a
:date: |date|

.. |date| date:: %B %d, %Y

:Copyright: Copyright (c) 2013 Dave Kuhlman.  All Rights Reserved.
    This software is subject to the provisions of the MIT License
    http://www.opensource.org/licenses/mit-license.php.

:Abstract: This document provides notes and guidance on the use of
           the materials in this directory for teaching a beginning
           class of Python programming.

.. sectnum::
.. contents::


Overview
==========

The contents of this archive/directory are intended to be used by an
instructor delivering a course on beginning Python.

This README gives a brief survey of where to find things in this
directory and its sub-directories and some guidance on how to use
the materials.

Documentation -- Look in the Docs directory.  A more detailed
description of the contents of that directory is below. 

Assignments and exercises -- In several directories you will find
pairs of files: a text (.txt) file and an HTML file (.html).
Usually, the HTML file was generated from the text file (the source)
using Docutils (http://docutils.sourceforge.net/).  Often these
documents give assignments and exercises that an instructor can give
to students to work on after the completion of a given topic.  There
is usually a solution (a Python module that solves the execercise),
which you can show to students and discuss after they have had time
to work on the exercise.  Often the solution is "hidden" in a
sub-directory named "Solutions".


How to use these Materials -- suggestions
-------------------------------------------

I carry these materials to class on CDs and flash drives.  On the
morning of the first day of class, I ask students to copy this
directory (``Materials``) onto their hard drive.

The latest version of these materials is available at my Web site:
http://www.davekuhlman.org/#materials-for-python-training

I teach most of the course from the notes in
``Docs/python_course_03.html``.

See section `Directory contents`_ for more detailed information on
the contents.


Modifying documentation (HTML) files
--------------------------------------

Many of the HTML files were produced using Docutils, which is a
documentation preparation system written in Python.  These HTML
files were generated from corresponding source text files containing
reStructuredText.  For example, the file "abc.txt" would be used to
generate "abc.html".

To do this, you will need the following:

- Install Docutils, if you do not already have it.  You can find it
  here: http://docutils.sourceforge.net/

- Learn some reStructuredText, although in many cases, you may be
  able to simply follow the layout, format, and indentation of an
  existing document (a ``.txt`` file).  There is documentation at
  the Docutils site, and a quick reference is here:
  http://docutils.sourceforge.net/docs/user/rst/quickref.html

Once Docutils is installed on your machine, you should be able to
re-generate an HTML file with the following::

    $ rst2html.py --stylesheet=Docs/pytraining_docutils.css abc.txt abc.html

The ``--stylesheet`` option is not strictly necessary, but will
produce output with an appearance more consistent with other HTML
files in these Materials.  The file ``pytraining_docutils.css`` is
in the ``Docs/`` directory, so you may need to adjust the above
command depending on your current directory.


Directory contents
====================

Here is a directory listing::

    Materials
    |-- Code_python                     # Code and exercises
    |   |-- Cmd
    |   |-- CommandLineOptions
    |   |-- ConfigParser
    |   |-- Database
    |   |-- Decorators
    |   |-- ExceptionSubclass
    |   |-- FixedLenRecords
    |   |-- Import
    |   |-- IteratorGenerator
    |   |-- Jython
    |   |-- Oop
    |   |   `-- Solutions
    |   |-- TextAndFiles
    |   |-- TreeStructure
    |   |-- Unittest
    |   |   `-- Solutions
    |   |-- VarialbeLenRecords
    |   |-- WrapperEnvelopeIterable
    |   |-- Xml
    |   |-- Zipfiles
    |   |-- package_sample1
    |   |   `-- sub_package
    |   `-- package_sample2
    |-- Docs
    |-- Exercises_python                # Exercises and assignments (see below)
    |   `-- Solutions
    |-- Samples_python                  # Other samples of Python code
    |-- Templates_python                # Starter templates for modules and scripts
    |-- Work                            # An empty directory for student work
    |-- bin                             # Files to set command line environment
    `-- python-2.7.6-docs-html          # The Python standard documentation (HTML)


Materials/Docs
----------------

Documentation to be used during training.

- ``agenda_4day.html`` -- An overview and schedule for a 4 day
  course.

- ``outline_03.pdf`` -- Slides to be used to introduce (and in some
  cases, summarize) various topics.

- ``python_book_01.html`` and ``python_book_01.pdf`` -- A Python
  course book.  Also available at http://www.lulu.com/shop/shop.ep
  and at my Web site http://www.davekuhlman.org.  You might consider
  printing this book as a hand-out to students, although I'm sure
  that there are better Python texts available.

- ``python_course_03.html`` -- The course notes that I use while
  teaching.  When I teach, I often have these open in a Web browser
  on my screen and in front of the students via an overhead
  projector.

- ``python_versions_01.txt`` -- During the first morning's
  introduction to Python, I show this on the screen while describing
  the different versions of Python.


Materials/Exercises_python
----------------------------

Exercises for various topics -- Solutions are in the ``Solutions``
sub-directory.  For example:

- ``numbers1.html`` -- Exercises on ints and floats.

- ``lists1.html`` -- Exercises for lists and tuples.

- ``strings1.html`` -- Exercises for strings.

- ``class_static_method.html`` --

- ``dictionaries1.html`` -- Exercises for dictionaries.

- ``files1.html`` -- Exercises on reading and writing text files.

- ``statements1.html`` -- Exercises for Python statements.

- ``functions1.html`` -- Exercises for defining and calling
  functions.

- ``classes1.html`` -- Exercises for object-oriented programming and
  implementing classes in Python.

 
Materials/Code_python
-----------------------

- ``Cmd`` -- Exercise -- Implement an interactive prompt using the
  ``cmd`` module.

- ``CommandLineOptions`` -- Exercise -- Parse and capture command
  line options using ``argparser`` and ``getopt``.

- ``ConfigParser`` -- Exercise -- Parse and write a ``.ini``
  configuration file.

- ``Database`` -- Exercise -- Create, write, and query/read a
  relational database using the ``sqlite3`` module.

- ``Decorators`` -- Exercise -- Implement a function that can be
  applied as a decorator to trace other functions.

- ``Import`` -- Sample -- Shows importing a module that imports a
  module, and demonstrates modifying a value that is global within a
  module.

- ``IteratorGenerator`` -- Exercise -- Implement a generator
  function -- a function the contains ``yield`` and, therefore,
  returns a generator (an iterable).

- ``Oop`` -- Exercise -- Implement a class hierarchy used to track
  and display a fleet of vehicles and their routes.

- ``package_sample1`` -- An example of a Python package that makes
  several objects global within the package.  To get an idea of what
  it does, do the following from the directory immediately above
  it::

        >>> import package_sample1 
        >>> print dir(package_sample1)

- ``package_sample2`` -- Similar to ``package_sample2``.

- ``TextAndFiles`` -- Exercises -- Specifically:

  - CSV -- Comma separated values -- Read and print a report from a
    CSV file.

  - Count words -- Assignment is in words.html.  Sample data is in
    words.dat.  There are several solutions; words3.py is preferred.

  - Various other exercises for string processing and text file
    processing.

- ``TreeStructure`` -- Exercise -- Create, walk, and display tree
  structures implemented with (1) lists, (2) dictionaries, and (3)
  instances of a custom class.

- ``Unittest`` -- (1) Samples of unit test classes and harnesses to
  run those tests.  (2) Exercise -- Implement a unit test class
  (sub-class of ``unittest.TestCase``) and a test harness to test
  several database access functions.

- ``Xml`` -- Exercise -- ``elementtree_walk.html`` for an exercise
  using ``xml.etree.ElementTree``.

- ``ExceptionSubclass`` -- Exercise -- Define an Exception subclass
  and catch it in a ``try:except:`` statement.  A similar exercise
  is in ``Exercises_python/statements1.html``.
  
- ``FixedLenRecords`` -- Write and read fixed length records,
  specifically text records that are *not* separated by newlines.

- ``VarialbeLenRecords`` -- Write and read variable length records,
  specifically text records that are *not* separated by newlines and
  where the record length is stored in the first bytes of each
  record.

- ``WrapperEnvelopeIterable`` -- 

- ``Zipfiles`` -- Exercise -- Create and process zip file archives
  using the ``zipfile`` module.


Materials/Samples_python
--------------------------

This directory contains samples of Python code.  It's the place
where I put sample files that I do not need immediately, but think
that I might, and that I don't want to throw away.

When you need a sample of code to illustrate some Python topic and
you can't find it in ``Exercises_python`` or ``Code_python``, you
might look for it here.

