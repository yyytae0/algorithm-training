def check():
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j < i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i][j-i] + lst[i], dp[i-1][j-i] + lst[i], dp[i-1][j])

    return dp[n][n]


n = int(input())
lst = [0] + list(map(int, input().split()))
ans = check()
print(ans)
