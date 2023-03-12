ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    dp = [[0, 0, 0] for _ in range((n//10)+1)]
    dp[1] = [1, 0, 0]
    dp[2] = [1, 1, 1]
    for i in range(3, (n//10)+1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        dp[i][1] = dp[i-1][0]
        dp[i][2] = dp[i-1][0]
    print(f'#{case}', sum(dp[n//10]))
