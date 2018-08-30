#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 exercises_30_8
#program: pentagon.py
#description: Help USA build da pentagon!

size = int(input('size: '))

for i in range(size):
    for space in range(size-i-1):
        print(' ',end='')
    for star in range(2*size-1+2*i):
        print('*',end='')
    print()

for i in range(size-1):
    for space in range((i+1)*2):
        print(' ',end='')
    for star in range(4*(size-1-i)-3):
        print('*',end='')
    print()
