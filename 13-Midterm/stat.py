# -*- coding: utf-8 -*-
#std35: Phitchawat Lukkanathiti 6110503371
#date: 4OCT2018
#program: stat.py
#description: basic stat calculation

def my_mean(iplist):
    return sum(iplist)/len(iplist)

def my_mode(iplist):
    count_list = {}
    for i in iplist:
        if i in count_list:
            count_list[i] += 1
        else:
            count_list[i] = 1
    mode_fre = sorted(count_list.values())[-1]
    mode = []
    for a, b in count_list.items():
        if b == mode_fre:
            mode.append(a)
    if len(mode) > 2:
        return 'None'
    mode = [str(x) for x in mode]
    return str(' and ').join(mode)

def my_med(iplist):
    iplist.sort()
    if len(iplist)%2 == 1:
        return iplist[(len(iplist)-1)//2]
    return (iplist[(len(iplist)-2)//2]+iplist[(len(iplist))//2])/2

ip = input('Input number : ')

number = [int(x) for x in ip.split()]

print(f'Max = {max(number)}')
print(f'Min = {min(number)}')
print(f'Mean = {my_mean(number):.2f}')
print(f'Mode = {my_mode(number)}')
print(f'Med = {my_med(number)}')
