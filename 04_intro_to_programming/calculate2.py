#! /usr/bin/python3
'''
def sumdigits(digits):
    x = 0
    y = 0
    answer = 0
    finalanswer = 0
    
    stdigits = str(digits)
    while x < len(stdigits):
        answer = int(stdigits[x]) + answer
        x += 1
    secondanswer = str(answer)
    if len(secondanswer) > 1:
        while y < len(secondanswer):
            finalanswer = int(secondanswer[y]) + finalanswer
            y += 1
    if finalanswer == 0:
        return answer
    else:
        return finalanswer

sumdigits(1235)
'''
'''
def calculate(x):
    answer = 0
    num_list = list(str(x))
    for num in num_list:
        answer = answer + int(num)
    return answer
'''

def calculate(x):
    answer = 0
    
    num_list = list(str(x))
    for num in num_list:
        answer = answer +int(num)
    if len(str(answer)) > 1:
        return(calculate(answer))
    return answer
calculate(1235)