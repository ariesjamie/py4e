#Write a program to read through a file and print the contents of the file (line by line) all in upper case. 

'''
input: a text file
output: a piece of text file and all UPPER case
'''

file = input('Please enter a file name: ')
file = open('mbox-short.txt')
try:
    file = open('mbox-short.txt')
except:
    print('file is not existed.')
    exit()

for content in file:
    content = content.rstrip()
    print(content.upper())
