#! /usr/bin/python3
unumber = input('Enter your number:')
if unumber is '':
    print('Please enter a number')
elif int(unumber) % 2 == 0:
    print('This is a even number')
else:
    print('This is a odd number')

