str='hello'

print(dir(str))

'hello'.islower()

'hello'.isupper()

ip_addr = "1.1.1.1/24"
print(ip_addr.replace("/"," /"))

#import requestprintstar
#from pprint import pprint
#r=requests.get('http://facebook.com/')
#requests.get('https://api.github.com/user', auth=('user', 'pass'))
#print('r attribute', dir(r))
#print('this is print ', r.json())
#pprint('this is pprint' + r.json())


def sum (a,b):
    return ( a + b )

def printstar(n):
    for i in range(1,n):
        print(i * "*")

printstar(5)