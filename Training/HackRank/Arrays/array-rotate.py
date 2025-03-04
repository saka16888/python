class arrayoperations():
    def reversearray(self,arr,n):
        n1=round(n/2)
        for i in range(n1):
            arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        return arr

    def leftrotate(self,arr,n,d):
        temp = arr[0]
        for i in range(n-1):
            arr[i-1+d]=arr[i+d]
            arr[i+d]=temp
        return arr

def rotLeft(a, d):
    n=len(a)
    d=d % n
    s=a[-n+d:]+a[:d]
    print('a=',a,'left rotate', d, ', result s=',s)
    return s

    t=list(a)
    n=len(a)
    d = d % n
    print("\na[%d:%d] = %r, a[:%d] = %r" % (d,n,a[d:n], d,a[:d]))
    t[:n-d], t[n-d:] = a[d:n], a[:d]
    print('a=',a,'left rotate',d,', t=',t)
    return t

def rotRight(a, d):
    t=list(a)
    n=len(a)
    d=d % n
    print("\na[%d:%d] = %r, a[:%d] = %r" % (d,n,a[d:n], d,a[:d]))
    t[:n-d], t[n-d:] = a[d:n], a[:d]
    print('a=',a,'left rotate',d,'t=',t)
    return t

def rotRight1(a, d):
    n=len(a)
    d=d%n
    s=a[-d:]+a[:n-d]
    print('a=',a,'right rotate ', d,', result s=', s)
    return s

arr=[2,3,4,6,1]
a2=[7,8]
print("\n\narr + a2 = ",arr + a2)
arr.extend(a2)
print('\narr.extend(a2) =',arr)
print(arr[1:4])
print(arr[3:0:-1])
print(arr[3::-1])

#=======
# print(arr[1:4])
# print(arr[0:4])

print(arr[0:5])
print("arr[2-5:]=",arr[2-5:])
print("arr[2-5::-1]=",arr[2-5::-1])
print(arr[:2:-1])
rotLeft(arr,0)
rotLeft(arr,1)

print(rotLeft(arr,5))
rotLeft(arr,6)
rotLeft(arr,-1)
rotLeft(arr,-2)
a3=rotRight(arr,2)
print("a3 = ",a3)

#=======
rotLeft(arr,5)
rotLeft(arr,6)
rotLeft(arr,7)

print('-' * 50)
arr1=arr
n=len(arr)
l1=arrayoperations()
x=l1.leftrotate(arr1,n,1)
print(arr1,"array after left rotate :",x)

#x=l1.leftrotate(arr,n,2)
#print(arr1,"array after left rotate :",x)

x=l1.reversearray(arr,n)
print(arr,"array after reversearray :",x)

tmp=arr.reverse()
print(arr,tmp)


