import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack,self.queue = [],[]

    def pushCharacter(self,ch):
        self.stack.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self,ch):
        self.queue.append(ch)

    def dequeueCharacter(self):
        return self.queue.pop(0)

s="hellol"
obj=Solution()
l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
for i in range(l//2):
    a = obj.popCharacter()
    b = obj.dequeueCharacter()
    print("a=",a,"b=",b)
    if a != b :
        isPalindrome=False
        break

if isPalindrome:
    print(s,"is Palindrome")
else:
    print(s, "is not Palindrome")