# -*- coding: utf-8 -*-
#std25: Phitchawat Lukkanathiti 6110503371
#date: 09AUG2018
#program: L01P5.py
#description: calculate number of salesman route

from math import factorial
input=int(input("How many cities? "))
print("For {} cities, there are {} possible routes".format(input,factorial(input)))