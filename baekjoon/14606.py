n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 0
for i in range(2, n+1):
    mx = 0
    for j in range(1, i):
        d = dp[j] + dp[i-j] + (i-j)*j
        if d > mx:
            mx = d
    dp[i] = mx
print(dp[n])