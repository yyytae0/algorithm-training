n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[0 for _ in range(n*100+1)] for _ in range(n+1)]
mn = 10000
for i in range(1, n+1):
    for j in range(n*100+1):
        dp[i][j] = dp[i-1][j]
        if j >= cost[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-cost[i-1]] + memory[i-1])
        if dp[i][j] >= m and j < mn:
            mn = j
print(mn)
