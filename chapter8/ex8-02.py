#Find all unique words in a file. Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand?
#Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

# Create a list of unique words, which will contain the final result. 
list = list()
# Write a program to open the file romeo.txt
file = open('romeo.txt')
# read it line by line. 
for line in file:
    line = line.rstrip()
# For each line, split the line into a list of words using the split function. 
    words = line.split()
    print(words)
# For each word, check to see if the word is already in the list of unique words.
    for word in words:
        if word not in list:
# If the word is not in the list of unique words, add it to the list. 
            list.append(word)
            print(list)
# When the program completes, sort and print the list of unique words in alphabetical order.
list.sort()
print(list)
