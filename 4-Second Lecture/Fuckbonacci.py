fibo=[1,1]
while True:
    fibo.append(fibo[-1]+fibo[-2])
    print(fibo[-1])
    if fibo[-1]//10**30 == 1:
        break
print("Index :",len(fibo)-1)
print("Fibo :",fibo[-1])
