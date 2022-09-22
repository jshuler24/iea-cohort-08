#! /usr/bin/python3
import random
space = 0
turns = 0

#start : end spaces of chutes & ladders
chutes_ladders = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44,
                  47:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                  71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

# main game - rolls dice adds it to your position, checks against chutes_ladders 
def game_play (max_roll=6):
    global space
    global turns
    while space < 100:
        turns += 1
        roll = random.randint(1,max_roll)

        if space + roll > 100:
            continue
        space += roll
        space = chutes_ladders.get(space,space)
        break

while space < 100:
    game_play()
    print(f'You landed on space {space}')