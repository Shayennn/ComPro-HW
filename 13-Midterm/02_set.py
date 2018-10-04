# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 4OCT2018 midterm
#program: 02_set.py
#description: Set calc without set()

def Union(X, Y):
    X = X.copy()
    Y = Y.copy()
    for each in Y:
        if each not in X:
            X.append(each)
    X.sort()
    return X

def Intersection(X, Y):
    X = X.copy()
    Y = Y.copy()
    Intersected = []
    for each in Y:
        if each in X:
            Intersected.append(each)
    return Intersected

def Delete(X, Y):
    X = X.copy()
    Y = Y.copy()
    for each in Y:
        if each in X:
            X.remove(each)
    X.sort()
    return X

def Complement(X):
    U = list(range(20))
    X = X.copy()
    for each in X:
        U.remove(each)
    return U

A=[int(c) for c in input('A: ').split()]
B=[int(c) for c in input('B: ').split()]
print('A U B:',Union(A,B))
print('A ^ B:',Intersection(A,B))
print('A - B:',Delete(A,B))
print('A\':',Complement(A))
