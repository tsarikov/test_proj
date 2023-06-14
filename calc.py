def operator(operand_1: int, operand_2: int, sign: str) -> float:
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
    
    
    i = 0
    while i < length_of_expression:
        if expression[i] in operators_list:
            result = operator(expression[i-2],expression[i-1],expression[i])
            expression[i-2] = result
            del expression[i]
            del expression[i-1]
            length_of_expression = len(expression)
            if i > 2:
                i -= 1
        else:
            i += 1

    return expression[0]

print(rpn_calc([1, 2, '+', 4, '*', 3, '+']))
print(rpn_calc([7, 2, 3, '*', '-']))
print(rpn_calc([8,7,9,3,77,'*','-','/',4,'+','*']))


    
                            