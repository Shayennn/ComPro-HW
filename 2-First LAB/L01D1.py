# -*- coding: utf-8 -*-
#std25: Phitchawat Lukkanathiti 6110503371
#date: 09AUG2018
#program: L01D1.py
#description: how long that it will take to calculate route?

import math
cities = int(input("Enter number of cities? "))
timetake = math.factorial(cities)/((10**6)*3600*24*365.25)
print("It will take %.4f years"%timetake)
