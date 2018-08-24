# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 22AUG2018
#program: L03P3.py
#description: if and no elif .....

status={90:'Senior Status',60:'Junior Status',30:'Sophomore Status',0:'Freshman Status'}

while True:
    credit = int(input("Enters the number of college credits earned : "))
    for credit_rule,std_status in status.items():
        if credit>credit_rule or credit_rule==0:
            print(std_status)
            break
