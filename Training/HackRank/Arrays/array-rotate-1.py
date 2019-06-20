class ArrayOperation:

    def __init__(self, arr):
        self.arr=arr
        self.len=len(arr)

    def printArray(self):
        print("self array ", self.arr)

    def reverse(self):
        print("self array reverse", self.arr.reverse() )
        return self.arr

    def reverse2(self):
        print("self array reverse2", self.arr.reverse() )
        s=self.arr
        return s

    def leftRotate(self,k):
        s=self.arr[-self.len+k:] + self.arr[:k]
        return s

    def leftRotate2(self,k):
        return (self.arr[-self.len+k:] + self.arr[:k])


    def rightRotate(self,k):
        return (self.arr[k : self.len -1] +self.arr[0:k])

def rotLeft(a, d):
    return

def rotRight(a, d):
    return

print("************-- 1 ***************************-")
arr=[2,3,4,6,1]
a1=ArrayOperation(arr)
print("array arr",arr)
a1.printArray()
print("reverse array ",a1.reverse()) # Question, why return None
print("reverse2 array ",a1.reverse2()," arr = ",arr)
print("reverse array",arr[::-1],"\n\n")

print("************-- 2 ***************************-")
arr=[2,3,4,6,1]
print("array arr",arr)
k=2
n=len(arr)
# arr[3,4,6,1,2] left rotate 1
a1=arr[k : n] +arr[0:k]
print("k=",k,", n=",n,", arr[k : n] =",arr[k : n],"arr[0:k] =",arr[0:k],", left rotate k position ", a1)

print("************-- 3 ***************************-")
# arr[6,1,2,3,4,] right rotate 2
arr=[2,3,4,6,1]
print("\narray arr",arr)
k=2
n=len(arr)
a2=arr[k:n]+arr[0:k]
print("k=",k,", n=",n,", arr[0:k] =",arr[0:k],"arr[k:n] =",arr[k:n],", right rotate k position ", a2)
print("right rotate k position ", a2)

print("************-- 4 ***************************-")
print("\n")
a2=[7,8]
print("arr + a2 = ",arr + a2)
arr.extend(a2)
print('arr.extend(a2) =',arr)

print("arr =",arr)
print(arr[1:4])
print("arr[0:5]=",arr[0:5])
print("arr[2-5:]=",arr[2-5:])
print("arr[2-5::-1]=",arr[2-5::-1])

print("************-- 5 ***************************-")
print(arr[:2:-1])
rotLeft(arr,0)
rotLeft(arr,1)
rotLeft(arr,5)
rotLeft(arr,6)
rotLeft(arr,-1)
rotLeft(arr,-2)
rotRight(arr,2)

arr1=arr
n=len(arr)
l1=ArrayOperation(arr1)
x=l1.leftRotate(1)
print(arr1,"array after left rotate :",x)

#x=l1.leftrotate(arr,n,2)
#print(arr1,"array after left rotate :",x)

x=l1.reverse()
print(arr,"array after reversearray :",x)

tmp=arr.reverse()
print(arr,tmp)


