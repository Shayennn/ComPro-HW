# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 6SEP2018 quiz03
#program: 01_leapyear.py
#description: check that is leapyear

year = int(input('year: '))

answer=False

if year%4==0:
    if year%100==0:
        answer=False
        if year%400==0:
            answer=True
    else:
        answer=True

if answer:
    print(year,'is leap year')
else:
    print(year,'is not leap year')
