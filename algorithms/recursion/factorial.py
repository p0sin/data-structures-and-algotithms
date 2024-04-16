# Write two functions that finds te factorial of any number.
# One should use recursive, the other should just use a for loop

def findFactorialRecursive(number): # O(n)
    # Base Case
    if number == 1:
        return number
    # Recursive Case
    else:
        return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number): # O(n)
    answer = 1
    for i in range(1, number + 1): 
        answer = answer * i
    return answer

x = findFactorialRecursive(5)
print(x)
y = findFactorialIterative(5)
print(y)