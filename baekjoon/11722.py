def check():
    dp = [1 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i):
            if lst[j] > lst[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


n = int(input())
lst = [0] + list(map(int, input().split()))
ans = check()
print(ans)
