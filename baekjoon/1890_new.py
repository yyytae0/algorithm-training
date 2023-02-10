n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if [i, j] == [n-1, n-1]:
            break
        dn = i + lst[i][j]
        rt = j + lst[i][j]
        if dn <= n-1:
            dp[dn][j] += dp[i][j]
        if rt <= n-1:
            dp[i][rt] += dp[i][j]

print(dp[n-1][n-1])
