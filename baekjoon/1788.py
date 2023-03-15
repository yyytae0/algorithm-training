n = int(input())
dp = [0 for _ in range(abs(n)+1)]
if n == 0:
    print(0)
    print(0)
    pass
elif n > 0:
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000000
    print(1)
    print(dp[n])
else:
    dp[1] = 1
    for i in range(2, -n+1):
        dp[i] = (dp[i-2]-dp[i-1])
        if dp[i] > 0:
            dp[i] = dp[i] % 1000000000
        else:
            dp[i] = -(-dp[i] % 1000000000)
    if dp[-n] > 0:
        print(1)
        print(dp[-n])
    else:
        print(-1)
        print(-dp[-n])
