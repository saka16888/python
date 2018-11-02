__author__ = 'mihung'

with open('./notes/stocks.txt',encoding='ascii' ) as f:
    for line in f:
        line=line.rstrip()
        lname, fname, title, email = line.split(',')
        #print(line)
        print(lname, fname, title, email)

