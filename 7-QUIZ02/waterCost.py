#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 exercises_30_8
#program: waterCost.py
#description: calculate water cost

unit = int(input("unit: "))

cost = 110

if unit > 40:
    cost+=(unit-40)*7
    unit=40
if unit > 20:
    cost+=(unit-20)*10
    unit=20
if unit > 7:
    cost+=(unit-7)*17
    unit=7

print('cost(Baht):',cost)
