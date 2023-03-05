n = int(input())
m = int(input())
lst = list(int(input()) for _ in range(m))
if n > 1:
    dp = [0 for _ in range(n + 1)]
    dp[0], dp[1] = 1, 1
    s = 0
    for i in range(m):
        g = lst[i]
        for j in range(s + 2, g):
            if j > 1:
                dp[j] = dp[j - 1] + dp[j - 2]
        dp[g] = dp[g - 1]
        if g != n:
            dp[g + 1] = dp[g - 1]
        s = lst[i]

    for i in range(s + 2, n + 1):
        if i > 1:
            dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])
else:
    print(1)
