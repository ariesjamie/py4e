#Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F


def computegrade():
    '''
    ##this function takes input of score and print the grade
    this function takes input of score and output the grade
    
    input: score
    output: print grade 
    '''

    #print('Result')
    if score > 1.0 or score < 0:
        return 'Bad request'
    elif score >= 0.9 and score < 1.0:
        return 'A'
    elif score >= 0.8 and score < 0.9:
        return 'B'
    elif score >= 0.7 and score < 0.8:
        return 'C'
    elif score >= 0.6 and score < 0.7:
        return 'D'
    else:
        return 'F'


def computegrade2():
    '''
    this function takes input of score and print the grade
    this function takes input of score and output the grade -> return the grade
    input: score
    output: grade 
    '''
    # input = score
    # output = grade
    grade = 'Bad request'
    #print('Result')

    if score > 1 or score < 0:
        return grade

    if score >= 0.9 and score < 1.0:
        grade = 'A'
    elif score >= 0.8 and score < 0.9:
        grade = 'B'
    elif score >= 0.7 and score < 0.8:
        # return 'C'
        grade = 'C'
    elif score >= 0.6 and score < 0.7:
        # return 'D'
        grade = 'D'
    else:
        # return 'F'
        grade = 'F'

    return grade

def computegrade3():
    '''
    this function takes input of score and print the grade
    this function takes input of score and output the grade -> return the grade
    input: score
    output: grade 
    '''
    # input = score
    # output = grade
    grade = 'Bad request'

    if score > 1 or score < 0:
        print('Result: ', grade)
        return 

    if score >= 0.9 and score < 1.0:
        grade = 'A'
    elif score >= 0.8 and score < 0.9:
        grade = 'B'
    elif score >= 0.7 and score < 0.8:
        # return 'C'
        grade = 'C'
    elif score >= 0.6 and score < 0.7:
        # return 'D'
        grade = 'D'
    else:
        # return 'F'
        grade = 'F'

    print('Result: ', grade)
     

enter_score = input('enter your score:')
score = float(enter_score)

final_result = computegrade2()
print('Result:', final_result)

