#Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, 
# then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

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
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
print(dict)
