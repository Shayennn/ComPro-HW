# -*- coding: utf-8 -*-
#std25: Phitchawat Lukkanathiti 6110503371
#date: 09AUG2018
#program: L01P4.py
#description: find dec base of 4-digits binary

first=int(input("Enter leftmost digit: "))
second=int(input("Enter next digit: "))
third=int(input("Enter next digit: "))
forth=int(input("Enter next digit: "))
result = first*8+second*4+third*2+forth
print("The value is {}".format(result))