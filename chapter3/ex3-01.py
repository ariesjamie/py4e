#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours

hours = float(input('please enter hours:'))
rate = float(input('please enter rate:'))
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
