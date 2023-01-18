def is_prime():
    prime = [True for _ in range(100001)]
    prime[1] = False

    m = int(100000 ** 0.5)
    for n in range(2, m + 1):
        if prime[n]:
            for k in range(n, 100001):
                if n * k > 100000:
                    break
                prime[n * k] = False
        if n * (n + 1) > 100000:
            break
    return prime


ip = list(map(int, input().split()))
cnt = 0
prime = is_prime()

d = [0 for _ in range(ip[1]+1)]

for i in range(1, ip[1]+1):
    if prime[i]:
        d[i] = 1
for i in range(2, ip[1]+1):
    for j in range(2, ip[1]+1):
        if i * j > ip[1]:
            break
        if prime[j]:
            d[i*j] = d[i] + 1


ans = 0
for i in range(ip[0], ip[1]+1):
    if prime[d[i]]:
        ans += 1

print(ans)

