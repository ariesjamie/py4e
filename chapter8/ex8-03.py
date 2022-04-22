#MBOX (mail box) is a popular file format to store and share a collection of emails. 
# This was used by early email servers and desktop apps. 
# Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
# Emails are separated by a special line which starts with From (notice the space). 
# Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
# Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

# input: a log file
# output: sort out all lines start with From and print out the From email address, also count the number of the From lines.

# Write a program to read through the mail box data
#list = list()
log_file = open('mbox-short.txt')
# when you find line that starts with “From”,
count = 0
for line in log_file:
    line = line.rstrip()
    if line.startswith('From:'):
# you will split the line into words using the split function. 
        words = line.split()
        print(words)
# We are interested in who sent the message, which is the second word on the From line.
# You will parse the From line and 
        email_add = words[1]
# print out the second word for each From line, 
        print(email_add)
# then you will also count the number of From (not From:) lines and
        count = count + 1
# print out a count at the end
print('There are', count, 'lines in the file with From as the first word')

