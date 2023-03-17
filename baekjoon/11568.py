n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n)]
ans = 1
for i in range(n):
    d = 0
    for j in range(0, i):
        if lst[j] < lst[i] and dp[j] > d:
            d = dp[j]
    dp[i] = d + 1
    if dp[i] > ans:
        ans = dp[i]
print(ans)
