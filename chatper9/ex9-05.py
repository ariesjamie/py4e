#This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

#open a file
file = open('mbox-short.txt')
#create an empty dictionary
domain_dict = dict()
#read the file
for line in file:
    #only read the line starts with "From"
    if line.startswith("From:"):
        #split the line into lists 
        words = line.split()
        #locate the second word in the list and split the word using by @
        word = words[1].split('@')
        #pass the content to domain 
        domain = word[1]
        #counting
        domain_dict[domain] = domain_dict.get(domain, 0) + 1
#print out result
print(domain_dict)
