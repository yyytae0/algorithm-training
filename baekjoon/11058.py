n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(1, min(7, n+1)):
    dp[i] = i

for i in range(6, n+1):
    for j in range(3, 6):
        if dp[i] < dp[i-j]*(j-1):
            dp[i] = dp[i-j]*(j-1)
print(dp[n])
