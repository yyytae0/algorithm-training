def check(i):
    if i == 1:
        return 0
    if dp[i-1]:
        return dp[i-1]
    dp[i-1] += check(lst[i])
    dp[i-1] += d[i]
    return dp[i-1]


n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
d = [0 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    d[a] += b
dp = [0 for _ in range(n)]
for i in range(2, n+1):
    if not dp[i-1]:
        check(i)
print(*dp)
