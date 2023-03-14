dp = [[0]]
dp.append([1])
dp.append([1, 1])
n, k = map(int, input().split())

for i in range(3, n+1):
    dummy = [1]
    for j in range(1, i-1):
        dummy.append(dp[-1][j]+dp[-1][j-1])
    dummy.append(1)
    dp.append(dummy)

print(dp[n][k-1])
