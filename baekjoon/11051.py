n, k = map(int, input().split())
total = 1

for i in range(n, 0, -1):
    total = total * i
    if i <= k:
        total = total/i

    if i <= n-k:
        total = total/i

print(int(total % 10007))
