r, c, w = map(int, input().split())
n = max(r+w, c+w)
dp = [[1 for j in range(i)] for i in range(n)]
for i in range(3, n):
    for j in range(1, i-1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

ans = 0
for i in range(r-1, r+w):
    for j in range(c-1, c+i-r):
        ans += dp[i][j]
print(ans)
