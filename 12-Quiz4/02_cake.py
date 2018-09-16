# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 13SEP2018 quiz04
#program: 02_cake.py
#description: print X cake

height = int(input('height: '))

for i in range(height):
    [print(' ',end='') for _ in range(height-i)]
    print('_'*(2*i+1),sep='')

    [print(' ',end='') for _ in range(height-i-1)]
    print('|',end='')
    print('X'*(2*i+1),sep='',end='')
    print('|')
