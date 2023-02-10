def check():
    dp = [([1]+[0 for _ in range(n)]) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

    return dp[k][n] % 1000000000


n, k = map(int, input().split())
ans = check()
print(ans)
