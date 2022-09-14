#! /usr/bin/python3
in_user = input('Please enter a 5 character string:')
in_length = len(in_user)
while (in_length != 5):
    in_user = input('Please enter a 5 character string:')
    in_length = len(in_user)