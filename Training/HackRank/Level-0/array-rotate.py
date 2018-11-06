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

arr=[2,3,4,6,1]
arr1=arr
n=len(arr)
l1=arrayoperations()
x=l1.leftrotate(arr,n,1)
print(arr1,"array after left rotate :",x)

x=l1.reversearray(arr,n)
print(arr,"array after reversearray :",x)

tmp=arr.reverse()
print(arr,tmp)


