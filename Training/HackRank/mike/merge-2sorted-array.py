def merge1(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()

def merge2(nums1, nums2):
    i,j = 0,0
    while i != len(nums1) and j != len(nums2):
        #print("i,j",i,j,nums1[i],nums2[j])
        if  nums1[i] >= nums2[j]:
            nums1.insert([nums2[j]])
            i=i+1
        j=j+1
    if i == len(nums1):
        nums1.extend(nums2[j::])
    print("nums1",nums1,"nums2",nums2)

a1=[1,2,4,7,8]
a2=[2,3,5,6]
merge1(a1,a2)
print("merge1 a1",a1,"a2",a2)

merge2(a1,a2)
print("merge2 a1",a1,"a2",a2)

def change_arg(a):

    print("count ",a.count(12))
    print("pop",a.pop(),a)
    print("remove", a.remove(2), a)
    print("reverse", a.reverse(), a)
    print("clear", a.clear(), a)
    print("clear", a.insert(0,[12,23]), a)
    a.extend([12])
    a=[23,44,55]

print("a1",a1)
change_arg(a1)
print("Update a1",a1)
