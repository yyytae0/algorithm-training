c, n, = map(int, input().split())
dp = [[float('inf') for _ in range(c+1)]]+[[0 for _ in range(c+1)] for _ in range(n)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    for j in range(1, c+1):
        if j < b:
            dp[i][j] = min(a*((j+b)//b), dp[i-1][j])
        elif j % b == 0:
            dp[i][j] = min(a*(j//b), dp[i-1][j], dp[i][j-b]+a)
        else:
            dp[i][j] = min(a*((j+b)//b), dp[i][j-b]+a, dp[i-1][j])
print(dp[n][c])
