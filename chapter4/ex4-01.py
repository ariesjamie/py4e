#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + ot_hours * ot_rate
        #print("You worked overtime. This is your gross pay", pay)
    else:
        pay = hours * rate
        #print("You didn't work overtime. This is your gross pay", pay)
    return pay

ehours = input('enter hours:')
erate = input('enter rate:')
hours = float(ehours)
rate = float(erate)
ot_hours = hours - 40
ot_rate = rate * 1.5

gross_pay = computepay(hours, rate)
print('This is your gross pay', gross_pay)

