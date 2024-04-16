# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 12, 21, 34, 55, 89, 144..
# The pattern of the sequence is that each value is the sum of the 2 previous values, that mean that for N = 5 -> 2 + 3

def fibonacciIterative(num):
    if num < 2:
        return num
    a = 0
    b = 1
    total = 0
    for i in range(num-1):
        total = a+b
        a = b
        b = total
    return total

def fibonacciRecursive(num):
    if num < 2:
        return num
    return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)
    
x = fibonacciRecursive(6)
print(x)
y = fibonacciIterative(6)
print(y)

# Recursion is best used when searching through trees or graphs
# Recursion rules