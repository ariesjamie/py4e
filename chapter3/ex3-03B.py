#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

enter_score = input('please enter a score:')
try:
    score = float(enter_score)
except:
    print('Sorry, please enter a valid score.')
    quit()

if score > 1.0 or score < 0:
    print('Error.')
elif score >= 0.9 and score < 1.0:
    print('Your grade is A')
elif score >= 0.8 and score < 0.9:
    print('Your grade is B')
elif score >= 0.7 and score < 0.8:
    print('Your grade is C')
elif score >= 0.6 and score < 0.7:
    print('Your grade is D')
#elif score < 0.6:
#    print('Unfortunately, you failed.')
#else:
#    print('Please enter a valid number')
else:
    print('You failed, please work hard.')
print('Exit')



