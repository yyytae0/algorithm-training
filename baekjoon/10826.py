n = int(input())
dp = [1 for _ in range(n+1)]
dp[0] = 0
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])