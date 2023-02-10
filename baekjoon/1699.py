n = int(input())
lst = []
cnt = 0
for i in range(1, int(n**(1/2))+1):
    lst.append(i**2)
    cnt += 1
dp = [[0 for _ in range(n+1)] for _ in range(cnt)]
for j in range(1, n+1):
    dp[0][j] = j
for i in range(1, cnt):
    for j in range(1, n+1):
        if lst[i] > j:
            dp[i][j] = dp[i-1][j]
        elif lst[i] == j:
            dp[i][j] = 1
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-lst[i]] + 1)

print(dp[cnt-1][n])
