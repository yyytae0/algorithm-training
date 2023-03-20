n = int(input())
dp = [0 for _ in range(10)]
dp[2] = 2
for i in range(3, 10):
    dp[i] = dp[i-1] * 3
print(dp[n])