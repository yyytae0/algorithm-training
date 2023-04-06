n, m, h = map(int, input().split())
dp = [[0 for _ in range(h+1)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    for j in range(h+1):
        dp[i][j] = (dp[i][j] + dp[i-1][j]) % 10007
        if dp[i-1][j]:
            for k in lst:
                if j + k > h:
                    break
                dp[i][j + k] = (dp[i][j+k] + dp[i-1][j]) % 10007
print(dp[-1][-1] % 10007)