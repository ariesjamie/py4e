# Write a program to look for lines of the form: New Revision : 39772
# Extract the number from each of the lines using a regular expression and the findall() method. 
# Compute the average of the numbers and print out the average as an integer.


def ave(list):
    '''
    input list
    output average number
    return average number

    '''
    ave = sum(list)/len(list)
    return ave

import re
file = open('mbox.txt')
num_list = list()
for line in file:
    line = line.rstrip()
    nums = re.findall("^New Revision: ([0-9]+)", line)
    for num in nums:
        num_list.append(int(num))
ave = ave(num_list)
print(ave)
#print('average is ', sum(num_list)/len(num_list))



