#! /usr/bin/python3

import random

ans_number = random.randint(1, 100)
in_number = int(input('Please take a guess between 1-100, you may enter 0 to quit:'))
ans_attempts = 1

while (in_number != ans_number):

    if (in_number == 0):
        break
    elif (in_number > ans_number):
        print('Your guess is too high, try again')
        in_number = int(input('Please take another guess between 1-100, you may enter 0 to quit:'))
        ans_attempts = ans_attempts + 1

    elif (in_number < ans_number):
        print('Your guess is too low, try again')
        in_number = int(input('Please take another guess between 1-100, you may enter 0 to quit:'))
        ans_attempts = ans_attempts + 1
    
if in_number == 0:
    print('Sorry you gave up')
else:
    print(f'You got it congrats, you took {ans_attempts} guesses!')