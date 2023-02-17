n = int(input())

prime = [1 for _ in range(10**6)]
for j in range(2, 5*(10**5)+1):
    if 2*j < 10**6:
        prime[2*j] = 0

if n == 1 or n == 2:
    print(2)
else:
    for i in range(3, 10 ** 6, 2):
        if prime[i]:
            if i < 1001:
                for j in range(2, 5 * (10 ** 5) + 1):
                    if i * j < 10 ** 6:
                        prime[i * j] = 0
            d = str(i)
            if d == d[::-1]:
                if i >= n:
                    print(i)
                    break
