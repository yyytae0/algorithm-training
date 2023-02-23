n, m = map(int, input().split())
now, next = 0, 1
for i in range(n-m):
    print(now, next)
    now += 1
    next += 1

for i in range(m-1):
    print(now, next)
    next += 1