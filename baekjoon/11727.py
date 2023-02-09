def check():
    dp = [[0, 0, 0] for _ in range(n+1)]
    dp[1] = [1, 0, 0]
    dp[2] = [1, 1, 1]
    for i in range(3, n+1):
        dp[i][0] = sum(dp[i-1]) % 10007
        dp[i][1] = sum(dp[i-2]) % 10007
        dp[i][2] = sum(dp[i-2]) % 10007

    return sum(dp[n]) % 10007


n = int(input())
if n == 1:
    print(1)
else:
    ans = check()
    print(ans)
