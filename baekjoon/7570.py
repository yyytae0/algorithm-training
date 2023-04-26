n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in lst:
    dp[i] = dp[i-1] + 1
# print(*dp)
print(n - max(dp))
