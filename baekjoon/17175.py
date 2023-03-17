n = int(input())
if n == 0:
    print(1)
else:
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + 1) % 1000000007
    print(dp[n])
