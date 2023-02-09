def check():
    dp = [0 for _ in range(n+1)]
    day = 1
    for i in lst:
        dp[day] = max(dp[day], dp[day-1])
        if day + i[0] - 1 <= n:
            dp[day + i[0] - 1] = max(dp[day + i[0] - 1], dp[day-1] + i[1])
        day += 1

    return dp[n]


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = check()
print(ans)
