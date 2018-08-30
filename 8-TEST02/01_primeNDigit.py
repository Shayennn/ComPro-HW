# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 quiz02
#program: 01_primeNDigit.py
#description: count prime that have n digits

n = int(input('n: '))

number_range = [True for _ in range(10**n)]

count=0

for number in range(10**n):
    if number_range[number]==False or number < 2:
        number_range[number]=False
        continue
    if number>=(1+10**(n-1)):
        count+=1
    for not_prime in range(number*2,10**n,number):
        number_range[not_prime]=False

print(count)
