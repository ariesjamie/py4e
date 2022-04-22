#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
'''
input: numbers
output: maximum and minimum of the numbers
'''
from cmath import inf

maxvalue = -float(inf)
minvalue = float(inf)
while True:
    number = input("Please enter a number:")
    if number == "done":
        print(maxvalue, minvalue)
        break
    try:
        num = float(number)
    except:
        print('Invalid input, try again.' )
        continue
    maxvalue = max(num, maxvalue)
    minvalue = min(num, minvalue)
    print(maxvalue, minvalue)
