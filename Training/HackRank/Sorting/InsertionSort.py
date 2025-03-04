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
print("Sorted array:", insertion_sort(a))


def insertion_sort2(arr):
    # Start from the second element (index 1) since the first element is trivially sorted
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are greater than key to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct location
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort2(arr)
print("Sorted array:", arr)
