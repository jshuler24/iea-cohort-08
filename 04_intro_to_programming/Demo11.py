#! /usr/bin/python3
is_prime = True
low_end = int(input('Please enter the low value of your prime number search:'))
high_end = int(input('Please enter the high value of your prime number search:'))

for num in range(low_end,high_end + 1):
    for i in range (2,num):
        if (num %i) == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{num}, is a prime number.')  
    else:
        is_prime = True

         
            
