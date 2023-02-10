def check():
    dp = [[0 for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        for j in range(1, k+1):
            if lst[i] > j:
                dp[i][j] = dp[i-1][j]
            elif lst[i] == j:
                dp[i][j] = 1
            else:
                if dp[i-1][j] and dp[i][j-lst[i]]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-lst[i]] + 1)
                elif dp[i-1][j] and not dp[i][j-lst[i]]:
                    dp[i][j] = dp[i-1][j]
                elif not dp[i-1][j] and dp[i][j-lst[i]]:
                    dp[i][j] = dp[i][j-lst[i]]+1

    return dp[n-1][k]


n, k = map(int, input().split())
lst = list(int(input()) for _ in range(n))
ans = check()
if ans:
    print(ans)
else:
    print(-1)
