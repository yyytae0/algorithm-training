from sys import stdin


n, m = map(int, stdin.readline().split())
lst = list(stdin.readline().strip() for _ in range(n))
check = list(stdin.readline().strip() for _ in range(m))
ans = 0
for i in check:
    l = len(i)
    for j in lst:
        if i == j[:l]:
            ans += 1
            break
print(ans)
