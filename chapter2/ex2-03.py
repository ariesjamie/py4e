#compute gr Write a program to prompt the user for hours and rate per hour to oss pay

hours = float(input('Please enter your hours:'))
rate = float(input('Please enter your rate per hour:'))
gross_pay = hours * rate
print('This is your gross pay', gross_pay)


# alternative way
hours = input('Please enter your hours:')
rate = input('Please enter your rate per hour:')
gross_pay = float(hours) * float(rate)
print('This is your gross pay', gross_pay)
