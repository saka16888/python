'''
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example,Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string s='abcac'  and n=10 , the substring we consider is 'abcacabcac',
the first  10 characters of her infinite string.
There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.
It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0
'''

def repeatedString(s,n):
    if n<=0: return ""
    l=len(s)
    m= (n//l) * s.count("a") + s[:n%l].count("a")
    #r= s* int(n/t+1); print(r[:n],'m=',m)
    return m

a="aba"
n=100
#print(n/3)
print(repeatedString(a,n))
print(repeatedString(a,4))
print(repeatedString(a,0))
print(repeatedString(a,-1))
print(repeatedString('a',1000))
#print(repeatedString('a',1000000000000))

