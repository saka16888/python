
arr1 = [int(tmp) for tmp in input().strip().split(' ')]
n=arr1[0]
arr1 = [int(tmp) for tmp in input().strip().split(' ')]
arr1_len=len(arr1)
zero_count = p_count = n_count = 0
for v in arr1:
    if v > 0 :
        p_count += 1
    elif v < 0:
        n_count = n_count + 1
    else:
        zero_count = zero_count + 1

print("%f\n%f\n%f\n" % (p_count/arr1_len, n_count/arr1_len, zero_count/arr1_len))