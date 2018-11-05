'''
for line in open("myfile.txt"):
    print(line, end="")

The problem with this code is that it leaves the file open
for an indeterminate amount of time
after this part of the code has finished executing.
This is not an issue in simple scripts,
but can be a problem for larger applications.
The with statement allows objects like files to be used in a way
that ensures they are always cleaned up promptly and correctly.
'''
filename = '../notes/team.txt'
with open(filename) as f:
    for line in f:
        print(line, end="")
        #print(line)
    print(filename, " is closed : ", f.closed)
print(filename, " is closed : ",f.closed)
f.close()

print('-' * 60)
with open(filename) as f2:
    hist = f2.read()
print(hist)
f2.close()

a="abc"
b="cdf"
c=[1,2,3,4]
print(a, end="")
print(b, end="")
print(c)
d2 = "".join((str(d)) for d in c)
print ("d2=",d2, end="")