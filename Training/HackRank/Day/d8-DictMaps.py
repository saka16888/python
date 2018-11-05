'''
Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output

sam=99912222
Not found
harry=12299933
'''
#
# def query(phone_book,key) :
#     if phone_book.get(key) != None :
#         tmp="{}={}".format(key,phone_book[key])
#         return tmp
#     else:
#         return "Not found"
n= int(input())
# n=3

# phone_book = {}
# for i in range(n):
#     line = [j for j in input().strip().split(" ")]
#     phone_book[line[0]] = line[1]
    # phone_book.update({line[0] : line[1]})
    #print(phone_book)
name_numbers = [input().split() for i in range(n)]
print(name_numbers)
phone_book = {k:v for k,v in name_numbers}
print(phone_book)

# phone_book = {'a' :2,'b':3,'c':5}

while True:
    try:
        line = input()
        if line in phone_book:
            print("%s=%s" % (line,phone_book[line]))
        else:
            print("Not found")
    except:
        break
