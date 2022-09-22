#! /usr/bin/python3
def calculate(x, y, operator):
    answer = None 
    if operator == '+':
        answer = x + y
    if operator == '/':
        try:
            answer = x / y
        except ZeroDivisionError:
            print('You cant divide by zero, try again')
    if operator == '*':
        answer = x * y
    if operator == '-':
        answer = x - y
    if operator == '%':
        answer = x % y
    if operator == '**':
        answer = x ** y
    if operator == '//':
        answer = x // y
    return answer

calculate(2,0,'/')