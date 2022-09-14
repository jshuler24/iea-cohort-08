#! /usr/bin/python3
import random 

user_attempts = 1
rand_word = random.choice(['Pizza','Apple','Earth','World', 'Chicken', 'Tacos', 'Hibachi', 'Orange', 'Donuts', 'Phone'])
guess_word = (list(rand_word))
random.shuffle(guess_word)

print('Guess the word below:')
print('' .join(guess_word))


user_guess = input('Your guess is:')

while True:
    if user_guess == rand_word:
        print('You got it congrats!')
        break
    else:
        user_guess = input('Your guess was wrong try again:')
        user_attempts = user_attempts + 1
   
print(f'It took you this many attempts: {user_attempts}!')