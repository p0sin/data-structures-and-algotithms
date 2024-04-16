def reverse(string):
    # Base Case
    if len(string) == 1:
        return string
    
    # Recursive Case
    else:
        x = string[0]
        return reverse(string[1:]) + x
    
y = reverse('arturo')
print(y)