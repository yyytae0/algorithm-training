ip = int(input())
dp = [[0]*10 for _ in range(65)]
dp[1] = [1]*10
for i in range(2, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])
for _ in range(ip):
    n = int(input())
    print(sum(dp[n]))
