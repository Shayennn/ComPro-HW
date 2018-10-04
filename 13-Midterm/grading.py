# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 4OCT2018
#program: grading.py
#description: grading calc

def my_mean(iplist):
    return sum(iplist)/len(iplist)

def my_sd(iplist):
    temp = 0
    mean = my_mean(iplist)
    for x in iplist:
        temp += (x-mean)**2
    sd = (temp/(len(iplist)-1))**0.5
    return sd

def what_grade(score,conds):
    for grade ,cond in conds.items():
        if score > cond:
            return grade
    return 'F'

scores = [int(x) for x in input('Scores: ').split()]

mean = my_mean(scores)
sd = my_sd(scores)
conds = {
    'A':mean+sd,
    'B':mean+sd/2,
    'C':mean-sd/2,
    'D':mean-sd
    }

grades = [what_grade(x,conds) for x in scores]

print(' '.join(grades))
