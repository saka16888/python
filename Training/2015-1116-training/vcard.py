__author__ = 'mihung'
''' An old, true, and sordid tale of Python
    featuring raisins, checkerboards, pushy relatives,
    business cards, and getting much needed rest.
'''
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
    for line in f:
        line = line.rstrip()
        lname, fname, title, email, phone = line.split(',')
        print(fname, lname, title, email, phone)
        vcard = vcard_template % (lname, fname, fname, lname, title, phone, email)
        with open('tmp.vcf', 'a') as vcard_file:
            vcard_file.write(vcard)
