n, m = map(int, input().split())
lst = list(list(map(int, input())) for _ in range(n))
dp = [[[0, 0] for _ in range(m+1)] for _ in range(n+1)]
mx = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if lst[i-1][j-1]:
            dp[i][j] = [dp[i-1][j][0]+1, dp[i][j-1][1]+1]
            mx = max(mx, min(dp[i][j]))
for i in dp:
    print(*i)
print(mx**2)
