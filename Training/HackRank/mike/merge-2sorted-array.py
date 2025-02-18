def merge1(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()

def merge2(nums1, nums2):
    i,j = 0,0
    print(nums1, nums2)
    while i != len(nums1) and j != len(nums2):
        print("i,j",i,j,"value",nums1[i],nums2[j])
        if nums1[i] >= nums2[j]:
            nums1.insert(i,nums2[j])
            j=j+1
        i=i+1
    if i == len(nums1):
        nums1.extend(nums2[j::])
    print("nums1",nums1,"nums2",nums2)

def merge3(nums1, nums2):
    i,j = 0,0
    print(nums1, nums2)
    while i != (l1 := len(nums1)) and j != (l2 := len(nums2)):
        print("i,j",i,j,"value",nums1[i],nums2[j],"l1,l2",l1,l2)
        if nums1[i] >= nums2[j]:
            nums1.insert(i,nums2[j])
            j=j+1
        i=i+1
    if i == len(nums1):
        nums1.extend(nums2[j::])
    print("nums1",nums1,"nums2",nums2)

a1=[1,3,4,8]
a2=[2,9,10]
merge1(a1,a2)
print("merge1 a1",a1,"a2",a2,"\n","="*40)
a1=[1,3,4,7,8]
a2=[2,5,6,9,10]
merge2(a1,a2)
print("merge2 a1",a1,"a2",a2,"\n","="*40)

a1=[1,3,4,7,8]
a2=[2,5,6,9,10]
merge3(a1,a2)
print("merge3 a1",a1,"a2",a2,"\n","="*40)

def change_arg(a):
    b=a
    c=a[:]
    print("count ",a.count(12))
    print("pop",a.pop(),a)
    print("remove", a.remove(3), a)
    print("reverse", a.reverse(), a)
    print("clear", a.clear(), a)
    print("insert", a.insert(0,[12,23]), a)
    a.extend([12])
    print("a",a,"b",b,"c",c)

print("a1",a1)
change_arg(a1)
print("Update a1",a1)
