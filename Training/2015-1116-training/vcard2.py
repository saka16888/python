__author__ = 'mihung'
''' An old, true, and sordid tale of Python
    featuring raisins, checkerboards, pushy relatives,
    business cards, and getting much needed rest.
'''

import csv
import requests

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Flat Grape Dr;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:%s
REV:20151117T195243Z
END:VCARD
'''

with open('vcard.csv', encoding='ascii') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        vcard = vcard_template % (lname, fname, fname, lname, title, phone, email)

        filename = '%s_%s.vcf' % (fname, lname)
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard)

root_url = 'https://chart.googleapis.com/chart?'
query = dict(cht='qr', chs='300x300', chl=vcard)
r = requests.get(root_url, query)
image = r.content

with open('tmp.png', 'wb') as image_file:
    image_file.write(image)
