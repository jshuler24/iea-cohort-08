#! /usr/bin/python3
def calculate(x, y, operator): 
    answer = None 
    import math
    from math import log

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
            b=int(x)
            c = int(y)
        except ValueError:
            print('Not a number!')
        else:
            answer = math.log(b,c)
    print(answer)

