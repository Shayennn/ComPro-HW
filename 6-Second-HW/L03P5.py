# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 22AUG2018
#program: L03P5.py
#description: display positive and negative of input

posneg=[0,0]

while True:
    number = int(input("Please input number : "))
    if number > 0:
        posneg[0]+=1
    elif number<0:
        posneg[1]+=1
    else:
        break

print("Positive :",posneg[0])
print("Negative :",posneg[1])
