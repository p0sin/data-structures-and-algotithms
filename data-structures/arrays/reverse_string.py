# Create a function that reverses a string:
# 'Hi My name is Andrei' should be:
# 'ierdnA si eman vM iH' 

def reverse(string):
    reverse_list = []
    for i in range(len(string) - 1, -1, -1):
        reverse_list.append(string[i])
      
    return ''.join(reverse_list)

   
x = reverse('Hi My name is Andrei')
print(x)

# string[::-1]

def reverse2(string):
    reverse_string = string[::-1]

    return reverse_string

y = reverse2('arturo')
print(y)


