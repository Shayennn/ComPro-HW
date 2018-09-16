n = int(input("n: "))

samrub = list(range(1,53))[::-1]

while len(samrub)>1:
    for _ in range(n):
        samrub.append(samrub.pop(0))
    samrub.pop(0)

print(samrub[0])
