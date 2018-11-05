import sys

whitespace=' '
'''
print("Hi" "hello")
print("Hi","hello")
'''
def  StairCase(n):
    for i in range(1,n+1):
        s=(n-i)*whitespace+i*'#'
        print(s)

if __name__ == '__main__':
    StairCase(6)
    StairCase(1)
