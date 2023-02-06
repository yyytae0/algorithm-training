n, m = map(int, input().split())
total, sub1, sub2 = 1, 1, 1
for i in range(1, n+1):
    total = total * i
    if i <= m:
        sub1 = sub1 * i

    if i <= n-m:
        sub2 = sub2 * i

print(int(total/(sub1*sub2)))
