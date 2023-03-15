n = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
ans = 1
for i in range(1, n):
    mx = 0
    for j in range(i):
        if lst[j] > lst[i] and dp[j] > mx:
            mx = dp[j]
    dp[i] = mx+1
    if dp[i] > ans:
        ans = dp[i]
print(n - ans)
