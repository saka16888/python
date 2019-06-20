m=3
n=5
# row 3 x 5 column
x0=[[0 for j in range(n)] for i in range(m)]
print("x0 = ", x0)

#myArray[4][2]=1
x0[2][3]=1
print("x0 = ",x0)

# row 2 x 5 column
x1=[x[:] for x in [[1] * 5] * 2]
print("x1 = ",x1)

# 3-D array
x2=[j for j in [i for i in [[1] * 4] * 2] * 3]
print("x2 = ",x2)

x3=[0] * 4
print("x3= ",x3)
x4=[x3] * 3
print("x4= ",x4)
x5=[x4] * 2
print("x5= ",x5)
x5[0][1][2]=2
print("x5= ",x5)
x5[1][2][3]=6
print("x5= ",x5)

li2=[x for x in [[1] * 5] * 2]
print(li2)

t1= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print("t1 = ",t1)

vec = [[1,2,3], [4,5,6], [7,8,9]]
v1=[num for elem in vec for num in elem]
print("v1 = ",v1)

matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

m2=[]
for i in range(4):
    tmp=[]
    for row in matrix:
        tmp.append(row[i])
    m2.append(tmp)
print("m2 = ",m2)

m1=[[row[i] for row in matrix] for i in range(4)]
print("m1 = ",m1)

