numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(array) - 1):
            number_1 = array[i]
            number_2 = array[i + 1]

            if number_1 > number_2:
                array[i] = number_2
                array[i + 1] = number_1
                swaps = True
    

bubbleSort(numbers)
print(numbers)