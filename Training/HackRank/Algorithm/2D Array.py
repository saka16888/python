n=6
x=0
y=[[x] * n]
print("y = ",y)
m1 = [x for x in [[x] * n] * n]
'''
for i in range(n):
 tmp = [int(x) for x in input().strip().split(" ")]
 m1[i]=tmp
'''

m1=[
[1,1,1,0,0,0],
[0,1,2,0,0,0],
[1,1,1,0,5,0],
[0,0,2,4,4,0],
[0,0,0,2,0,0],
[0,0,1,2,4,0]]
print("m1 = \n",m1)
print("m1[:] = ", m1[:])
for x in m1:
    print("x = ",x)
    #print("x[:] = ", x[:])
print("m1[1][2] = ", m1[1][2])
print("m1[3][2] = ", m1[3][2])

list_sum=[]
for i in range(n-2):
    for j in range(n-2):
        tmp = (m1[i][j] + m1[i][j+1] + m1[i][j+2] +
            m1[i+1][j+1] +
            m1[i+2][j] + m1[i+2][j+1] + m1[i+2][j+2])
        print("sum[%d][%d] = %d" % (i,j,tmp))
        list_sum.append(tmp)

print("list_sum = ",list_sum,"\nmax sum = ",max(list_sum))
