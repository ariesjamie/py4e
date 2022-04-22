#Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary. It doesn’t matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

#open a file
file = open('words.txt')
#create an empty dict
dict = dict()
count = 0
#read file line by line
for line in file:
#split the line into words and store the words to lists
    words = line.split()
    for word in words:
        count = count + 1
        ##the value of the key will be overwritten by the duplicate item's value if the following if statement is not there. 
        if word in dict:
            continue
        dict[word] = count
#print out the result 
print(dict)
#check if the word is existed in dict, if not add to dictionary

