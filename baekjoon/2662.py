n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
dp = [[[0 for _ in range(m+1)] for _ in range(m)] for _ in range(n+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        d = lst[j-1][i]
        for k in range(n-j+1):
            nd = d + dp[k][i - 2][0]
            if dp[j+k][i-2][0] > dp[j+k][i-1][0]:
                dp[j+k][i-1] = dp[j+k][i-2][:]
            if nd > dp[j+k][i-1][0]:
                dp[j+k][i-1] = dp[k][i-2][:]
                dp[j+k][i-1][0] += d
                dp[j+k][i-1][i] = j
# for i in dp:
#     print(*i)
print(dp[n][-1][0])
print(*dp[n][-1][1:])
