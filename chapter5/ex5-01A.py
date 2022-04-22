#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
'''
input: numbers
output: the total, count, average of the numbers
'''

count = 0
sum = 0
while True:
    enumber = input("Please enter a number:")
    if enumber == "done":
        print(count, sum, sum/count)
        break
    #count = count + 1
    try:
        sum = sum + float(enumber)
        count = count + 1
    except:
        print('Invalid input, try again.' )
    #sum = sum + float(enumber)
print('Bye')
