n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[10][0] = 1
for i in range(11, n+1):
    for j in range(10):
        if j == 9:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][0])
            continue
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
print(sum(dp[n]))
d = 0
for i in range(1, n+1):
    d += sum(dp[n])
print(d)
