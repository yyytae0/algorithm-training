n = int(input())
lst = list(int(input()) for _ in range(n))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
# print(dp)
print(n-max(dp))
