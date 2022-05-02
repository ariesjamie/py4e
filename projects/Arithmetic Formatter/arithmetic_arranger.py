def arithmetic_arranger(problem_list, argument = False):
    if len(problem_list) > 5:
        return("Error: Too many problems.")

    operand_lists = []

    for i in range(len(problem_list)):
        str_list = problem_list[i].split()  

        if str_list[0].isdigit() == False or str_list[2].isdigit() == False: 
            return('Error: Numbers must only contain digits.')

        if len(str_list[0]) >= 5 or len(str_list[2]) >= 5:
            return("Error: Numbers cannot be more than four digits.")

        if str_list[1] not in ['+' ,'-']:
            return("Error: Operator must be '+' or '-'.")
        elif str_list[1] == "+":
            sum_results = int(str_list[0]) + int(str_list[2])
        elif str_list[1] == "-":
            sum_results = int(str_list[0]) - int(str_list[2])
        
        str_list.append(str(sum_results))
        operand_lists.append(str_list)
    

    for j, operand_list in enumerate(operand_lists):
        len_max = max(len(operand_list[0]), len(operand_list[2])) + 2
        if j == 0:
            line1 = ' ' * (len_max - len(operand_list[0])) + operand_list[0]
            line2 = operand_list[1] + ' ' * (len_max - 1 - len(operand_list[2])) + operand_list[2]
            line3 = '-' * len_max
            if argument:
                line4 = ' ' * (len_max - len(operand_list[3])) + operand_list[3]
        else:
            line1 += ' ' * 4 + ' ' * (len_max - len(operand_list[0])) + operand_list[0]
            line2 += ' ' * 4 + operand_list[1] + ' ' * (len_max - 1 - len(operand_list[2])) + operand_list[2]
            line3 += ' ' * 4 + '-' * len_max
            if argument:
                line4 += ' ' * 4 + ' ' * (len_max - len(operand_list[3])) + operand_list[3]
    
    output1 = line1 + '\n' + line2 + '\n' + line3
    if argument:
        output2 = output1 + '\n' + line4
        return output2
    else:
        return output1
    
problem_list = ["32 - 698", "3801 - 2", "45 + 43", "123 + 49", "11 + 9"]
result = arithmetic_arranger(problem_list, True)

print(result)
