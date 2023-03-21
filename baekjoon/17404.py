n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
dp = [[[0, 0, 0] for _ in range(3)] for _ in range(n)]
dp[0] = [[float('inf'), lst[0][0], lst[0][0]], [lst[0][1], float('inf'), lst[0][1]], [lst[0][2], lst[0][2], float('inf')]]
for i in range(1, n):
    for j in range(3):
        dp[i][0][j] = min(dp[i-1][1][j], dp[i-1][2][j]) + lst[i][0]
        dp[i][1][j] = min(dp[i-1][0][j], dp[i-1][2][j]) + lst[i][1]
        dp[i][2][j] = min(dp[i-1][1][j], dp[i-1][0][j]) + lst[i][2]

mn = 10**6
for i in range(3):
    if dp[n-1][i][i] < mn:
        mn = dp[n-1][i][i]
print(mn)
