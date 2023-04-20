from sys import stdin


n = int(stdin.readline())
lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for j in range(2, n):
    if not lst[0][j]:
        dp[0][j][0] += dp[0][j - 1][0] + dp[0][j - 1][1]
for i in range(1, n):
    for j in range(2, n):
        if not lst[i][j]:
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2]
            if not lst[i-1][j] and not lst[i][j-1]:
                dp[i][j][1] += sum(dp[i - 1][j - 1])

print(sum(dp[n-1][n-1]))