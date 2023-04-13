dp = [[0, 0, 0, 0] for _ in range(31)]
dp[1] = [0, 1, 1, 0]
dp[2] = [1, 2, 1, 1]
for i in range(3, 31):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = sum(dp[i-1]) + dp[i-2][0]
    dp[i][2] = dp[i-1][1]
    dp[i][3] = dp[i-1][1] + dp[i-1][3]


n = int(input())
while n:
    print(dp[n][1])
    n = int(input())
