first=int(input("Enter first number : "))
second=int(input("Enter second number : "))

while True:
    count+=1
    (first,second) = (second,first) if second>first else (first,second)
    first=first%second
    if first==0:
        print("GCD is",second)
        break
