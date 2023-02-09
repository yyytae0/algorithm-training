def check():
    dp = [0 for _ in range(k+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < lst[i]:
                dp[j] = dp[j]
            elif j == lst[i]:
                dp[j] = dp[j] + 1
            else:
                dp[j] = dp[j] + dp[j-lst[i]]

    return dp[k]


n, k = map(int, input().split())
lst = [0] + list(int(input()) for _ in range(n))
ans = check()
print(ans)
