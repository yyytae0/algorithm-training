n = int(input())
lst = list(map(int, input().split()))
t = []
mx = 0
dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = max(dp[i-1]+lst[i], lst[i])
    if dp[i] > mx:
        mx = dp[i]
    if lst[i] < 0:
        t.append(i)
print(t)
dp[-1] = 0
for i in t:
    d = lst[i]
    lst[i] = 0
    for j in range(i, n):
        dp[j] = max(dp[j - 1] + lst[j], lst[j])
        if dp[j] > mx:
            mx = dp[j]
            print(j, mx)
            print(dp)
    lst[i] = d
print(mx)
