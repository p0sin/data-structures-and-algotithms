numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
 
insertion_sort(numbers)
print(numbers)

