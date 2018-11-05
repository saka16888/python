
arr = [int(tmp) for tmp in input().strip().split(' ')]
x1=arr[0]
v1=arr[1]
x2=arr[2]
v2=arr[3]

while True:
    print ("x1 = ",x1," x2= ",x2)
    if (x1 == x2):
        print("YES")
        break
    elif ((v1 > v2) and ( x1 > x2)) or ((v1 < v2) and ( x1 < x2)):
        print("NO")
        break
    x1 += v1
    x2 += v2
