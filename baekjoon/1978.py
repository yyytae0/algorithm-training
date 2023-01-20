prime = [True] * 1001
prime[0] = False
prime[1] = False

for i in range(2, 50):
    for j in range(2, 500):
        if i * j > 1000:
            continue

        else:
            prime[i*j] = False

ip = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if prime[i]:
        cnt += 1

print(cnt)
