from sys import stdin


n, m = map(int, stdin.readline().split())
dp = [[0 for _ in range(m+1)] for _ in range(n)]
for i in range(n):
    a, b, c = map(int, stdin.readline().split())
    for j in range(m+1):
        dp[i][j] = dp[i-1][j]
        for k in range(1, c+1):
            if j < a*k:
                break
            dp[i][j] = max(dp[i][j], dp[i-1][j-a*k] + b*k)
print(dp[-1][-1])

# 시간초과
#
#
#
#
# n, m = map(int, stdin.readline().split())
# dp = [[0 for _ in range(m+1)] for _ in range(n)]
# for i in range(n):
#     a, b, c = map(int, stdin.readline().split())
#     for j in range(m+1):
#         for k in range(1, c + 1):
#             x, y = a * k, b * k
#             if x > j:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j])
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-x]+y, dp[i][j])
# print(dp[-1][-1])
#
# # 시간초과