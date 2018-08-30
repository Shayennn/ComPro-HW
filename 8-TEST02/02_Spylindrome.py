# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 quiz02
#program: 02_Spylindrome.py
#description: find nearest oct palindrome

def dec2oct_list(number):
    oct_list = []
    while number>0:
        oct_list.append(number%8)
        number//=8
    return (oct_list[::-1])

def is_palindrome(inlist):
    return inlist==inlist[::-1]

pos_int = int(input('Positive Integer: '))

paddingnumber=0
while True:
    if is_palindrome(dec2oct_list(pos_int+paddingnumber)):
        print(pos_int+paddingnumber)
        break
    if is_palindrome(dec2oct_list(pos_int-paddingnumber)):
        print(pos_int-paddingnumber)
        break
    paddingnumber+=1
