n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
dp = [0 for _ in range(n+1)]
for i in range(1, n):
    dp[i] = dp[i-1] + lst[i-1]
for i in range(n):
    for j in range(i, n+1):
        if dp[j]-dp[i-1] == m:
            cnt += 1
        elif dp[j]-dp[i-1] > m:
            break

print(cnt)
