def testfile(filename):
    st = ["abc", "deb", "abb"]
    with open (filename, 'w') as f:
        for i in st:
            f.write (i+"\n")
    f.close ()

    with open (filename, 'r') as f2:
        buf = f2.read ()
        print ("buf = \n",buf)
    f2.close ()

    s2 = {'1232', '24vf', '23ew'}
    with open (filename, 'a') as f3:
        print("append ",s2)
        for i in s2:
            f3.write (i+"\n")
    f3.close ()

    with open (filename, 'r') as f4:
        buf = f4.read ()
        print (buf)
    f4.close ()


filename = '../notes/team.txt'
testfile (filename)
