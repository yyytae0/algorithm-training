d, k = map(int, input().split())
dp = [0 for _ in range(d+1)]
dp[d] = k
for i in range(k//2, k+1):
    dp[d-1] = i
    for j in range(d-2, 0, -1):
        dp[j] = dp[j+2] - dp[j+1]
        if dp[j] <= 0:
            break
    else:
        if dp[1] > dp[2]:
            continue
        print(dp[1])
        print(dp[2])
        break
