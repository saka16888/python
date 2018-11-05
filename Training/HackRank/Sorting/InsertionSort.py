def insertion_sort(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            print(lst)
        lst[j + 1] = temp
    return lst

a=[7,5,6,3,2,1]
print(insertion_sort(a))

