# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 6SEP2018 quiz03
#program: 02_frog.py
#description: simulate frog jumping in to the pool

final_pos = int(input('distance: '))
frog_pos = []
movement = 1
start_at = 0
frog_step = 1
while True:
    frog_pos += [int(0.5*frog_step*(frog_step+1)*movement+start_at)]
    frog_step+=1
    if (frog_pos[-1] > final_pos and movement==1) or (frog_pos[-1] < final_pos and movement==-1):
        movement *= -1
        start_at = frog_pos[-1]
        frog_step=1
    elif (frog_pos[-1] == final_pos):
        break

[print(x,end=' ') for x in frog_pos]
print()
print("frog jumps",len(frog_pos),"time(s)")
