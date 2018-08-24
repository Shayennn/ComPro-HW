# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 22AUG2018
#program: L03D4.py
#description: Home Loan Amortization

loan=int(input("Loan amount : "))
term=int(input("Term (in year) : "))

print('Interest Rate\t\tMonthly Payment')
for interest in range(3,19):
    r=interest/12/100
    n=term*12
    d=(((1+r)**n)-1)/(((1+r)**n)*r)
    print('    ',interest,'%\t\t    ',format(loan/d,'.2f'))
