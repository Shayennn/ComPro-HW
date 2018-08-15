# Solution by Nuttaphong

number = int(input("Enter Max : "))

prime_ar = [True for _ in range(0,number+1)]
prime_ar[1]=False

for prime in range(1,number+1):
    if not prime_ar[prime]:
        continue
    for _ in range(2*prime,number+1,prime):
        prime_ar[_]=False

primes=[n for n in range(0,number+1) if prime_ar[n]]
print(sum(primes))
