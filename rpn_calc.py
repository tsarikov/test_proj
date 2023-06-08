def operator(operand_1, operand_2, sign):
    match sign:
        case '-':
            return operand_1 - operand_2
        case '+':
            return operand_1 + operand_2
        case '/':
            return operand_1 / operand_2
        case '*':
            return operand_1 * operand_2



def rpn_calc(expression):
    operators_list = ['+','-','/','*']
    length_of_expression = len(expression)
    
    for i in range(length_of_expression):
        if expression[i] in operators_list:
            result = operator(expression[i-2],expression[i-1],expression[i])
        expression[i-2] = result
        del expression[i-1]
        del expression[i]
                            