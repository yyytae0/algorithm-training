n = int(input())
if n == 1:
    print('SK')
else:
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[2] = 1
    for i in range(4, n + 1):
        dp[i] = 1 - max(dp[i - 1], dp[i - 3], dp[i - 4])
    if dp[n]:
        print('CY')
    else:
        print('SK')
