# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 22AUG2018
#program: L03M7.py
#description: lease coin

# Coin Change Exercise Program

import random

#	program greeting
print('The purpose of this exercise is to enter a number of coin values')
print('that add up to to a displayed target value.\n')
print('Enter coins values as 1-penny, 5-nickel, 10-dime, 25-quarter and 50-half')
print("Hit return after the last entered coin value.")
print ('--------------')

#	init
terminate = False
empty_str = ''

coins={'1':0,'5':0,'10':0,'25':0,'50':0}

#	start game
while not terminate:
    amount = random.randint(1,99)
    print('Enter coins that add up to', amount, 'cents, one per line.\n')
    game_over = False
    total = 0
    while not game_over:
        valid_entry = False

        while not valid_entry:
            if total == 0:
                entry = input('Enter first coin: ')
            else:
                entry = input('Enter next coin: ')

            if entry in (empty_str,'1','5','10','25','50'):
                if entry!=empty_str:
                    coins[entry]+=1
                valid_entry = True
            else:
                print('Invalid entry')

        if entry == empty_str: 
            if total == amount:
                half=amount//50
                quarter=(amount%50)//25
                dime=(amount%25)//10
                nickel=(amount-(half*50+quarter*25+dime*10))//5
                penny=(amount-(half*50+quarter*25+dime*10+nickel*5))
                if list(coins.values()) == [penny,nickel,dime,quarter,half]:
                    print('Correct!')
                else:
                    print('Correct but you don\'t enter least coins.')
                    print(coins.values())
                    print([penny,nickel,dime,quarter,half])
            else:
                print('Sorry - you only entered', total, 'cents.')
            game_over = True
        else:
            total = total + int(entry)
            if total > amount:
                print('Sorry - total amount exceeds', amount, 'cents.')
                game_over = True
    
        if game_over:
            entry = input('\nTry again (y/n)?: ')

            if entry == 'n':
                terminate = True

print('Thanks for playing ... goodbye')
