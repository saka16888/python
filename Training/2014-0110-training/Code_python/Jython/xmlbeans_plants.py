#!/usr/bin/env python

"""
Demonstration of XMLBeans generated API on plants XML instance document.

Usage:
    python xmlbeans_plants.py [options] command infilename.xml
Options:
    -h, --help      Display this help message.
Commands:
    c, create       Create a new catalog (XML document) and enter plants.
    a, add          Add plants to an existing catalog/document.
    d, display      Display the plants in a catalog
Example:
    python xmlbeans_plants.py create plants.xml
    python xmlbeans_plants.py add plants.xml
    python xmlbeans_plants.py d plants.xml
"""


#
# Imports:
import sys
import getopt
import time
from java.io import File
from org.apache.xmlbeans import XmlOptions
from org.openuri.domain.plantCatalog.plnt import \
     PlantCatalogDocument, PlantCatalog, \
     Plant

#
# Global variables and constants:



#
# Functions for external use, factories, etc:



#
# Classes:



#
# Functions for internal use:

def create_plant_catalog(outfilename):
    doc = PlantCatalogDocument.Factory.newInstance()
    catalog = doc.addNewPlantCatalog()
    current_date = time.ctime()
    catalog.setCreationDate(current_date)
    add_data(catalog)
    outfile = File(outfilename)
    opts = XmlOptions()
    opts.setSavePrettyPrint()
    opts.setSavePrettyPrintIndent(4)
    doc.save(outfile, opts)
    return doc


def add_plant_to_catalog(infilename):
    infile = File(infilename)
    doc = PlantCatalogDocument.Factory.parse(infile)
    catalog = doc.getPlantCatalog()
    add_data(catalog)
    opts = XmlOptions()
    opts.setSavePrettyPrint()
    opts.setSavePrettyPrintIndent(4)
    doc.save(infile, opts)
    return doc


def add_data(catalog):
    input_data = enter_plant_data()
    while input_data is not None:
        name, desc, id = input_data
        id = int(id)
        plant = catalog.addNewPlant()
        plant.setName(name)
        plant.setDescription(desc)
        plant.setId(id)
        input_data = enter_plant_data()

def enter_plant_data():
    name = raw_input('Plant name:        ')
    if len(name) == 0:
        return None
    desc = raw_input('Plant description: ')
    id = raw_input('Plant ID:          ')
    return name, desc, id


def display_info(infilename):
    infile = File(infilename)
    doc = PlantCatalogDocument.Factory.parse(infile)
    #print doc
    catalog = doc.getPlantCatalog()
    creationdate = catalog.getCreationDate()
    print 'Catalog -- created: "%s"' % (creationdate, )
    plants = catalog.getPlantArray()
    for plant in plants:
        show_plant(plant)


def show_plant(plant):
    name = plant.getName()
    desc = plant.getDescription()
    id = plant.getId()
    print 'Plant:'
    print '    Name:        %s' % (name, )
    print '    Description: "%s"' % (desc, )
    print '    ID:          %d' % (id, )


def test(command, filename):
    """Modify or replace this function for your own needs.
    """
    if command in ('c', 'create'):
        create_plant_catalog(filename)
    elif command in ('a', 'add'):
        add_plant_to_catalog(filename)
    elif command in ('d', 'display'):
        display_info(filename)
    else:
        raise RuntimeError, 'invalid command: "%s"' % command


USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'h', ['help',
             ])
    except:
        usage()
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
    if len(args) != 2:
        usage()
    command = args[0]
    filename = args[1]
    test(command, filename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


