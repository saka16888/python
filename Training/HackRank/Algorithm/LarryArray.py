
def rotate(list1, n):
    n = n % len(list1)
    return list1[n:] + list1[:n]

def robot_sort(arr_in):
    if (len(arr_in) < 3):
        return False
    arr_sorted = sorted(arr_in)
    len_arr=len(arr_in)
    all_arr = arr_in
    for i in range(2,len_arr):
        if (len_arr < i+1) :
            return False
        pat=arr_in[(i-2):(i+1)]
        #print("arr_in = %s,  arr_in[%d:%d] = %s" %
        #      (arr_in, i-2,i+1,arr_in[(i-2):(i+1)]))
        pat_sorted = False
        for j in range(3):
            #print("rotate pat = ", pat)
            if (pat[0] <= pat[1]) and (pat[1] <= pat[2]) :
                pat_sorted = True
                break
            else:
                pat = rotate(pat,1)

        if pat_sorted:
            print("all_arr = ", all_arr, "pat = ",pat)
            all_arr[(i-2):(i+1)] = pat
            print("all_arr = ",all_arr)
            if (all_arr == arr_sorted):
                return True
    return False

if __name__ == '__main__' :

    if False:
        n_in = [int(tmp) for tmp in input().strip().split(' ')]
        n = n_in[0]
        num=[]
        arr1=[]
        for i in range(n):
            in_num = [int(tmp) for tmp in input().strip().split(' ')]
            num.append(in_num[0])
            arr_in = [int(tmp) for tmp in input().strip().split(' ')]
            arr1.append(arr_in)

    arr1 = [[3, 1, 2], [1, 3, 4, 2],[1,8,5,7,13,11,12]]
    # arr1 = [[9,6,8,12,3,7,1,11,10,2,5,4],
    #         [17,21,2,1,16,9,12,11,6,18,20,7,14,8,19,10,3,4,13,5,15],
    #         [5,8,13,3,10,4,12,1,2,7,14,6,15,11,9]]
    for s1 in arr1:
        if robot_sort(s1):
            print("YES")
        else:
            print("NO")