def check(a):
    if dp[a]:
        return
    mx = 0
    for i in d[a][1]:
        if not dp[i]:
            check(i)
        if mx < dp[i]:
            mx = dp[i]
    dp[a] = mx + d[a][0]


n = int(input())
d = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for i in range(n):
    lst = list(map(int, input().split()))
    t = lst[0]
    cnt = lst[1]
    d[i+1] = [t, lst[2:2+cnt]]
for i in range(n, 0, -1):
    check(i)
print(max(dp))
