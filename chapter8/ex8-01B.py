#write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(y):
    '''
    This function takes a list and returns a new list that contains all but the first and last elements
    input: a list
    output: a list which removes the first element and the last element
    note: the original list will be unmodified and the output should be a new list
    '''
    return y[1:-1]

l = ['a', 'b', 'c', 'hello', 'world', '123']
new_l = middle(l)
print(l)
print(new_l)
