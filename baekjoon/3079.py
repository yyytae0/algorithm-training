n, m = map(int, input().split())
# lst = list(int(input()) for _ in range(n))
dp = []
for i in range(n):
    a = int(input())
    dp.append([a, 0])
dp.sort()
for i in range(m):
    d = dp[0][1] + dp[0][0]
    for j in range(1, n):
        if dp[j][1] + dp[j][0] < d:
            dp[j][1] += dp[j][0]
            break
    else:
        dp[0][1] += dp[0][0]
mx = 0
for i in dp:
    if i[1] > mx:
        mx = i[1]
print(mx)
