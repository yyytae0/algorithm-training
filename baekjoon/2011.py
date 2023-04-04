def check():
    if a[0] == '0':
        return 0
    n = len(a)
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if a[i-1] == '0':
            if int(a[i-2]) > 2 or int(a[i-2]) == 0:
                return 0
            else:
                dp[i] = dp[i-2]
        else:
            dp[i] = dp[i-1]
            if 10 <= int(a[i-2:i]) <= 26:
                dp[i] = (dp[i] + dp[i-2]) % 1000000
    return dp[n] % 1000000


a = input()
print(check())
