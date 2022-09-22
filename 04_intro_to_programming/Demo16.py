#! /usr/bin/python3
'''
userword = input('Enter a string:')
userstride = input('Enter a stride:')
i = 0
x = 0
for character in (userword.lower()):
    if x == 0:
        userword = userword.replace(character,character.upper())
        i += 1
        if i == int(userstride):
            i = 0
            x = 1
            continue
    if x == 1:
        userword = userword.replace(character,character.lower())
        i += 1
        if i == int(userstride):
            i = 0
            x = 0

print( f'with a stride of {userstride}. you get:', userword)
'''

