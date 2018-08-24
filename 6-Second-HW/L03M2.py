unit=['K','C','F','R']

def temp2kelvin(temp,inunit):
    if inunit == 0:
        return temp
    elif inunit == 1:
        return temp+273.15
    elif inunit == 2:
        return ((temp+459.67)*5/9)
    elif inunit == 3:
        return ((temp-7.5)*40/21+273.15)
    return -999

def kelvin2temp(kelvin,outunit):
    if outunit == 0:
        return kelvin
    elif outunit == 1:
        return kelvin-273.15
    elif outunit == 2:
        return (kelvin*9/5-459.67)
    elif outunit == 3:
        return ((kelvin-273.15)*21/40+7.5)
    return -999

print("Temperature choices are")
for unitnumber in range(len(unit)):
    print(unitnumber,").",unit[unitnumber])

inunit = int(input("Choose input unit number : "))
intemp = float(input("Input temperature : "))
outunit = int(input("Choose output unit number : "))
print("Temperature in ",unit[outunit],' is ',format(kelvin2temp(temp2kelvin(intemp,inunit),outunit),'.2f'))
