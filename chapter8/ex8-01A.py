#Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(x):
    '''
    This function takes a list and modifies it, removing the first and last elemetns and returns to None.
    we know the element that we wnat to remove (but not the index), so we choose to use 'remove'
    input: a list
    output: a list which removes the first element and the last element
    note: the original list will be modified
    '''
    x.remove(x[0])
    x.remove(x[-1]) 

l = ['a', 'b', 'c', 'hello', 'world', '123']
chop(l)
print(l)
