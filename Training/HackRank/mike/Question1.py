'''
How do you reverse a string?
How do you determine if a string is a palindrome?
How do you calculate the number of numerical digits in a string?
How do you find the count for the occurrence of a particular character in a string?
How do you find the non-matching characters in a string?
How do you find out if the two given strings are anagrams?
How do you calculate the number of vowels and consonants in a string?
How do you total all of the matching integer elements in an array?
How do you reverse an array?
How do you find the maximum element in an array?
How do you sort an array of integers in ascending order?
How do you print a Fibonacci sequence using recursion?
How do you calculate the sum of two integers?
How do you find the average of numbers in a list?
How do you check if an integer is even or odd?
How do you find the middle element of a linked list?
How do you remove a loop in a linked list?
How do you merge two sorted linked lists?
How do you implement binary search to find an element in a sorted array?
How do you print a binary tree in vertical order?
'''

a1="abc"
print(a1[::-1])

def ispalindrome(s):
    return s==s[::-1]

print(ispalindrome("abc"))
print(ispalindrome("aba"))

#How do you calculate the number of numerical digits in a string?
def countDigit2(s):
    return sum([d.isdigit() for d in s])
print("countDigit2",countDigit2("adsa121"))

#How do you calculate the number of numerical digits in a string?
def countDigit(s):
    count=0
    for d in s:
         if d.isdigit():
             count=count+1
    return count

def countDigit3(s):
    #for d in s:
    #    print(d.isdigit())
    total= [d.istitle() for d in s]
    print(total,sum(total))
    return sum(d.isdigit() for d in s)

print(countDigit("ads12"))
print(countDigit3("ads1434"))

s="adsvs2433sad"
print("string count", s.count("a"))

def collectlower(s):
    #for d in s:
    #    print(d.isdigit())
    total= [d.islower() for d in s]
    print(total)
    return sum(d.islower() for d in s)

a=5
b=5
print(a == b)
print(a is b)

print("#How do you find the count for the occurrence of a particular character in a string?")
a="sdfdsabcfew abcfgab"
b="abkl"
print(a.count(b))

print("#How do you find the non-matching characters in a string?")
print(set(a) ^ set(b))

#How do you find out if the two given strings are anagrams?
print("anagrams",a,sorted(a),b,sorted(b),sorted(a) == sorted(b))

#How do you calculate the number of vowels and consonants in a string?
def num_vowels_consonants(s):
    print(s)
    t=[c.lower() in "aeiou" for c in s]
    print(t)
    vowels=sum(c.lower() in "aeiou" for c in s)
    consonant=sum(c.isalpha() for c in s)
    return vowels, consonant
n,m=num_vowels_consonants(a)
print("n=",n,"m=",m,num_vowels_consonants(a))

#How do you total all of the matching integer elements in an array?
a1=[12,23,45,13,24,13,25]
def sum_all_match(num, target):
    return sum(n for n in num if n== target)
print(sum_all_match(a1, 13))

#How do you reverse an array?
print(a1[::-1])

#How do you find the maximum element in an array?
#a1.sort()
#print(a1[-1])
print(max(a1))
print(min(a1))

#How do you find the middle element in an array?
a1=[12,23,24,45,35]
print('a1=',a1)
print(a1[(len(a1)-1)//2])
print(round(0.5))
print(round(0.6))
print(round(-0.5))
print(round(-0.6))

s1="abc"
print([c for c in s1])

#How do you sort an array of integers in ascending order?
print(a1.sort())
print(a1)

#How do you print a Fibonacci sequence using recursion?
def fin(n):
    if n<2:
        #print(n)
        return(n)
    #print(n)
    return fin(n-1) + fin(n-1)
print(fin(5))

# Fibonacci series:
# the sum of two elements defines the next
def fin2(n):
    if n<2: return n;
    a, b = 0, 1
    for i in range(n+1):
        print(a,end=',')
        a, b = b, a+b
    return b-a
n=10
print("fin2(n)",n,fin2(n))

#How do you calculate the sum of two integers?
#How do you find the average of numbers in a list?
def average_sum(num):
    print("num",num)
    return sum(num)/len(num)

print("average_sum", average_sum(a1))

#How do you check if an integer is even or odd?
def is_even(n):
    return n % 2 == 0
a=124
print(is_even(a))


#How do you find the middle element of a linked list?
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

#How do you remove a loop in a linked list?

#How do you merge two sorted linked lists?
def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next

#How do you implement binary search to find an element in a sorted array?
def binary_search(arr, target):
    print("binary_search ",a1,target)
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low=mid+1
        else:
            high=mid-1
    return -1

a1=[12,23,34,45,56,67,78]
print(binary_search(a1,45))
print(binary_search(a1,24))

#How do you print a binary tree in vertical order?
from collections import defaultdict
def vertical_order(root):
    if not root:
        return []
    column_table = defaultdict(list)
    queue = [(root, 0)]
    min_column = max_column = 0
    while queue:
        node, column = queue.pop(0)
        column_table[column].append(node.val)
        min_column = min(min_column, column)
        max_column = max(max_column, column)
        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))
    return [column_table[i] for i in range(min_column, max_column + 1)]
