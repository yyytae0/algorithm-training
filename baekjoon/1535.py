n = int(input())
loss = list(map(int, input().split()))
get = list(map(int, input().split()))
dp = [[0 for _ in range(101)] for _ in range(n+1)]
mx = 0
for i in range(1, n+1):
    for j in range(100, -1, -1):
        if j > loss[i-1]:
            dp[i][j-loss[i-1]] = max(dp[i-1][j-loss[i-1]], dp[i-1][j] + get[i-1])
        else:
            dp[i][j-loss[i-1]] = dp[i-1][j-loss[i-1]]
print(dp[-1][1])
