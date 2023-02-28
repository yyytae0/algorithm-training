n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
if n % 2:
    print(0)
else:
    cnt = 0
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = 3 * dp[i-2] + (dp[i-2] - dp[i-4])
        cnt += 1
    print(dp[n])