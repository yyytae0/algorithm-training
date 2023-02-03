n, k = map(int, input().split())
total = 1
sub1 = 1
sub2 = 1
for i in range(1, n+1):
    total = total * i

    if i <= k:
        sub1 = sub1 * i

    if i <= n-k:
        sub2 = sub2 * i

print(int((total/(sub1*sub2) % 10007)))
