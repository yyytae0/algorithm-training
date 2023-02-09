n, k = map(int, input().split())
total = 1
dv = 1

for i in range(n, 0, -1):
    if i <= k:
        pass
    else:
        total = total * i

    if i <= n-k:
        dv = dv * i

print((total//dv) % 10007)
