#Google Question
#Given an array, return the first recurring character
#Example1 : array = [2,1,4,2,6,5,1,4]
#It should return 2
#Example 2 : array = [2,6,4,6,1,3,8,1,2]
#It should return 6

def first_recurring_char(array, dict):
    for char in array:
        if char in dict:
            return char
        else:
            dict[char] = True
    return None

array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
dict = {}

x = first_recurring_char(array, dict)
print(x)