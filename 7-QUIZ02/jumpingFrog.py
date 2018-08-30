#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 exercises_30_8
#program: jumpingFrog.py
#description: when the frog will reach the other riverside.

import math

h = int(input("h: "))
m = int(input("m: "))
n = int(input("n: "))

print(math.floor(h/(m-n)),'day(s)')
