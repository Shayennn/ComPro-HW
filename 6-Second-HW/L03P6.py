# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 22AUG2018
#program: L03P6.py
#description: display 1-100 10 per row

i=0
j=1

while i<10:
    while j<=10:
        print(i*10+j,end=' ')
        j+=1
    print()
    i+=1
    j=1
