a = input()
b = input()
na = len(a)
nb = len(b)
dp = [[[0, ''] for _ in range(nb+1)] for _ in range(na+1)]
for i in range(na):
    for j in range(nb):
        if a[i] == b[j]:
            dp[i+1][j+1][0] = dp[i][j][0] + 1
            dp[i+1][j+1][1] = dp[i][j][1] + a[i]
        else:
            if dp[i][j+1][0] > dp[i+1][j][0]:
                dp[i+1][j+1] = dp[i][j+1][:]
            else:
                dp[i + 1][j + 1] = dp[i+1][j][:]
print(dp[-1][-1][0])
print(dp[-1][-1][1])
