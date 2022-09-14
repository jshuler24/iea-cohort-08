#! /usr/bin/python3
in_num = int(input('Please enter a number:'))
in_ans = 1
for x in range(1,in_num+1):
    in_ans = in_ans*x
print(f'the factorial of {in_num}, is {in_ans}')  