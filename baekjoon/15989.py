dp = [[0, 0, 0] for _ in range(10001)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 0, 1]
for i in range(4, 10001):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-2][1] + dp[i-2][2]
    dp[i][2] = dp[i-3][2]
ip = int(input())
for _ in range(ip):
    n = int(input())
    print(sum(dp[n]))
