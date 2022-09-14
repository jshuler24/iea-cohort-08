#! /usr/bin/python3
user_string = input('please enter a string:')
for character in user_string [:-1]:
    print(character, '+', sep ='', end ='')
print(user_string[-1])