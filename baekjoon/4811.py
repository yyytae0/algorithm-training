dp = [0 for _ in range(31)]
dp[0] = 1
dp[1] = 1
for i in range(2, 31):
    for j in range(i):
        dp[i] += dp[j]*dp[i-j-1]
n = int(input())
while n:
    print(dp[n])
    n = int(input())