# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 4OCT2018 midterm
#program: 01_money_change.py
#description: Money Change For Resturant

NotesAndCoins = {1000:0, 500:0, 100:0, 50:0, 20:0, 10:0, 5:0, 1:0}

FoodsPrice = {'A':16, 'B':32, 'C':64, 'D':128}

def CustomerIn(Price):
    Nac = list(NotesAndCoins.keys())
    Nac.sort()
    for Recive in Nac:
        if Recive>Price:
            return Recive

def Foods2Price(Foods):
    Price = 0
    for Food in Foods:
        Price += FoodsPrice[Food]
    return Price

def Change(Recive,Price):
    LeftChange = Recive-Price
    ChangeNAC = {}
    for Nac in NotesAndCoins.keys():
        ChangeNAC[Nac] = LeftChange//Nac
        LeftChange %= Nac
    return ChangeNAC

def UpdateNAC(Getting):
    for Nac, Amount in Getting.items():
        NotesAndCoins[Nac] -= Getting[Nac]
    return NotesAndCoins

TodaySold = 0

for _ in range(int(input('n: '))):
    Order = input().split()
    Price = Foods2Price(Order)
    Recive = CustomerIn(Price)
    NotesAndCoins = UpdateNAC({Recive:-1})
    MustChange = Change(Recive,Price)
    NotesAndCoins = UpdateNAC(MustChange)
    TodaySold += Price

NACLeft = NotesAndCoins.values()
NACLeft = [str(x) for x in NACLeft]
print(' '.join(NACLeft))
print(TodaySold)
