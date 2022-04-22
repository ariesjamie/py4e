# Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
# 1. ^Author   2. ^X-    3. java$

import re
count = 0
file = open('mbox.txt')
reg_exp = input('Enter a regular expression:')
for line in file:
    line = line.rstrip()
    if re.findall(reg_exp, line):
        count = count + 1
print(count)
