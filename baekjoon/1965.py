n = int(input())

lst = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(n):
    mx = 0
    for j in range(i):
        if lst[j] < lst[i]:
            if dp[j] > mx:
                mx = dp[j]
    dp[i] = mx+1
print(max(dp))