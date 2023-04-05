from sys import stdin


n, m = map(int, stdin.readline().split())
dp = [[0 for _ in range(m+1)] for _ in range(n)]
chk = []
for i in range(n):
    a, b, c = map(int, stdin.readline().split())
    for j in range(m+1):
        k = 1
        while k <= c:
            x, y = a * k, b * k
            if k == c:
                x, y = a, b
            chk.append([x, y])
            if x > j:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-x]+y, dp[i][j])
            k *= 2
print(dp[-1][-1])

# 시간초과