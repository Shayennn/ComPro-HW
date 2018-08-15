number=int(input("Choose your number : "))

square = number

while True:
    last = square
    square = 0.5*(square+number/square)
    if abs(last-square) < 10**-20:
        print("Square :",square)
        break
