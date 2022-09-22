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
    if operator =='log':
        try:
            import math
            from math import log
            b=int(x)
            c = int(y)
        except ValueError:
            print('Not a number!')
        else:
            answer = math.log(b)/log(c)
    return answer

calculate(2,0,'/')