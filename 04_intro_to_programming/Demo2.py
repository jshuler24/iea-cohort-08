#! /usr/bin/python3
age = input('Enter your age:')
if age is '':
    print('Please enter your age:')
elif int(age) >= 21:
    print('You are of legal drinking age')
else:
    print('You are not old enough to drink')
