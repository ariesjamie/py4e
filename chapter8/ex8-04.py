# Rewrite the program that prompts the user for a list of numbers and 
# prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
from cmath import inf

num_max = float(-inf)
num_min = float(inf)
num_list = list()
while True:
    num = input('please enter a number:')
    if num == "done":
        print(num_max, num_min)
        break
    try:
        num = float(num)
    except:
        print('Invalid input. Enter a number again.')
# Write the program to store the numbers the user enters in a list and 
    if num not in num_list:
        num_list.append(num)
        print(num_list)
# use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
    num_max = max(num, num_max)
    num_min = min(num, num_min)
    print(num_max, num_min)
    print(num_list)




