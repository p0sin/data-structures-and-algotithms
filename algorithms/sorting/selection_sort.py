numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(array):
    for i in range(len(array)):
        min_value = array[i]
        hold = array[i]

        for j in range(i, len(array)):
            current = array[j]

            if min_value > current:
                min_value = current
                index = j
        
        array[i] = min_value
        array[index] = hold 

selection_sort(numbers)
print(numbers)
