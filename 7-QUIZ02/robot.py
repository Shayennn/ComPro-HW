#std35: Phitchawat Lukkanathiti 6110503371
#date: 30AUG2018 exercises_30_8
#program: robot.py
#description: vector size finding ?

command = input('commands: ')

i=0
j=0

for k in range(len(command)):
    if command[k] == 'N':
        j+=1
    elif command[k] == 'S':
        j-=1
    elif command[k] == 'E':
        i+=1
    elif command[k] == 'W':
        i-=1

distance = (i**2+j**2)**(1/2)
print("distance:",format(distance,'.2f'))
