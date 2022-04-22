# Revise a previous program as follows: Read and parse the “From” lines 
# and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read,
# print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.


from audioop import reverse
from itertools import count

#Read and parse the "From" lines, pull out the addresses from the line
file = open('mbox-short.txt')
dict = dict()
for line in file:
    if line.startswith("From"):
        words = line.split()
        word = words[1]
        #count the number of messages from each person using a dictionary
        dict[word] = dict.get(word, 0) + 1
#print(dict)

#create an empty list
tuple_list = list()
#print(tuple_list)
max_count = 0
max_email = None
for email,count in dict.items():
    #create a new list of (count, email)
    new_tuple = (count, email)
    tuple_list.append(new_tuple)
    #print(new_list)
#sort the list in reverse order
tuple_list = sorted(tuple_list, reverse = True)
#print(tuple_list)

#version 1: print out the person who has the most commits
person_tuple = tuple_list[0]
print(person_tuple[0], person_tuple[1])

#version 2: print out the person who has the most commits
for count,email in tuple_list[:1]:
    print(count, email)

#version 3: print out the person who has the most commits
for count,email in tuple_list:
    print(count, email)
    if count > max_count:
        max_count = count
        max_email = email
print('The person who has the most commits:', max_count, max_email)


##shorter version
# list = list()
# list = sorted([(count,email) for email, count in dict.items()])
# print(list)
