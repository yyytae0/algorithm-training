def check():
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j % lst[i] == 0:
                dp[i][j] += 1
            if j > lst[i]:
                dp[i][j] += dp[i][j-lst[i]]+dp[i-1][j]
            else:
                dp[i][j] += dp[i-1][j]

    return dp


n, k = map(int, input().split())
lst = [0] + list(int(input()) for _ in range(n))
ans = check()
print(ans)
