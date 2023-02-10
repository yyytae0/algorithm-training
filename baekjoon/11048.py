def check():
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + lst[i-1][j-1]

    return dp[n][m]


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = check()
print(ans)
