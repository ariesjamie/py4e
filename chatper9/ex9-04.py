# Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages 
# and print how many messages the person has.

#open a file
file = open('mbox-short.txt')
#create an empty dictionary
dict = dict()
#set initial count number 
count = 0
#read file by a for loop
for line in file:
    #only read lines starting with "From"
    if line.startswith('From:'):
        #split those lines into lists
        words = line.split()
        #look for the second word
        word = words[1]
        #decide if the second word is already existed in dictionary, if it is, add count, if not, count = 1
        dict[word] = dict.get(word,0) + 1
#print result
print(dict)

#look through the dictionary using a maximum loop to find who has the most messages 
#set initial maximum times 
maximum_times = 0
#set initial maximum email address 
maximum_email_add = None
#do a maximum comparison using a for loop
for word in dict:
    if dict[word] > maximum_times:
        maximum_times = dict[word]
        maximum_email_add = word
#print result
print('The most message sender:', maximum_email_add, maximum_times)
