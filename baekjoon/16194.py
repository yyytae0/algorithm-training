n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    mn = 10**7
    for j in range(0, i):
        d = dp[j] + lst[i-j-1]
        if d < mn:
            mn = d
    dp[i] = mn
print(dp[n])
