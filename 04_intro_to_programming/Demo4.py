#! /usr/bin/python3

in_year = int(input('Enter a Year:'))

if (in_year % 400 == 0) and (in_year % 100 == 0):
    print (f'{in_year} This is a leap year')

elif (in_year % 4 == 0) and (in_year % 100 != 0):
    print (f'{in_year} This is a leap year')
else:
    print (f'{in_year} This is not a leap year')

