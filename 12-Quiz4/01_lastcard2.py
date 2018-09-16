# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 13SEP2018 quiz04
#program: 01_lastcard2.py
#description: EZier version of lastcard

n = int(input('n: '))

deck = list(range(1,53))[::-1]

for _ in range(n):
    deck.append(deck.pop(0))
    if _+1==n:
        print(deck[0])
    del deck[0]
