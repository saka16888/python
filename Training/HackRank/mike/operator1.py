a=13
print("a=",a%3)
print("a=",a**2)

print(r'Walrus Operator :=')
# x := expression

#x := 10  # ❌ SyntaxError (must be inside an expression)
#
x=5
print(x:=10)
a1=[1,3,6]

#Using := in a While Loop
'''
data = input("Enter: ")
while data != "exit":
    print(f"You entered: {data}")
    data = input("Enter: ")
'''

while (data := input("Enter: ")) != "exit":
    print(f"You entered: {data}")

#Example 2: Using := in List Comprehensions
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums if x**2 > 10] # calculate x**2 twice
print(squares)  # Output: [16, 25]

# Avoids redundant calculations (x**2 is computed only once per iteration).
square=[sq for x in nums if ((sq := x**2) > 10)]
print(square)

