n = int(input())
dp = [1.0 for _ in range(n+1)]
mx = 1
for i in range(1, n+1):
    a = float(input())
    dp[i] = max(dp[i-1]*a, a)
    if dp[i] > mx:
        mx = dp[i]
print(f'{mx:.3f}')
