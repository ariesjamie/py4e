# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

##hours = float(input('please enter hours:'))
enter_hours = input('please enter hours:')
##rate = float(input('please enter rate:'))
enter_rate = input('please enter rate:')
try:
    hours = float(enter_hours)
    rate = float(enter_rate)
except:
    print('The number you entered is not a valid numeric input, please make sure you enter numeric input and try again.')
    quit()

overtime_hours = hours - 40
overtime_rate = rate * 1.5
if hours > 40:
    print('You worked overtime')
    pay = 40 * rate + overtime_hours * overtime_rate
else:
    print('You don''t have overtime pay')
    pay = hours * rate
print(hours, rate, overtime_hours, overtime_rate)
print('This is your pay in total:', pay)
