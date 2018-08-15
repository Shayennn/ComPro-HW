maxprime=int(input("Enter your max of sum :"))

prime=[]

def isPrime(n):
    global prime
    if n != 2 and n%2==0:
        return False
    if n in prime:
        return True
    for each_prime in prime:
        if n%each_prime==0 or each_prime>n:
            return False
    prime.append(n)
    return True

for i in range(2,maxprime+1):
    if isPrime(i):
        print(i,"is prime number.")

print("Sum :",sum(prime))
