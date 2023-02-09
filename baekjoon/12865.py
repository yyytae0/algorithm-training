def check():
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if lst[i][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], lst[i][1] + dp[i-1][j-lst[i][0]])

    return dp[n][k]


n, k = map(int, input().split())
lst = [[0, 0]] + list(list(map(int, input().split())) for _ in range(n))
ans = check()
print(ans)
