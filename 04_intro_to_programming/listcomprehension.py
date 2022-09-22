#! /usr/bin/python3

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
sleeves = ['short' , 'long']
tshirts = [[color, size, sleeve] for color in colors
                                  for size in sizes
                                  for sleeve in sleeves]
tshirts


answer = [x * x for x in range(1,26)]
answer


words = ['something', 'hello', 'goodbye', 'long']
wordlist = [[word] for word in words if word[-1] not in 'aeiou']
wordlist


numbers = range(1,100)
new_numbers = [[number] for number in numbers if number %5 != 0]
new_numbers
