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
print(dict)
