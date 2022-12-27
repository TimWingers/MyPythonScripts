def math_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

value1 = int(input('Введите 1е число: '))
value2 = int(input('Введите 2е число: '))
operator = input('Введите знак операции (+, -, *, /): ')
math_op(operator, value1, value2)