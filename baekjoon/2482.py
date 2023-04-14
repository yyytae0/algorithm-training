def check():
    for i in range(1, k + 1):
        if 2 * (i-1) >= n:
            print(0)
            return
        dp[i][2 * (i - 1)] = 1
        for j in range(2 * (i - 1) + 1, n - 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 2]) % 1000000003
        dp[i][n - 1] = dp[i][n - 2]
    print(sum(dp[k]) % 1000000003)
    return


n = int(input())
k = int(input())
dp = [[0 for _ in range(n)] for _ in range(k+1)]
dp[1] = [1 for _ in range(n)]
check()
