def check():
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1] = [1, 0, 0]
    dp[2] = [1, 1, 0]
    dp[3] = [2, 1, 1]
    for i in range(4, n+1):
        dp[i][0] = sum(dp[i-1])
        dp[i][1] = sum(dp[i-2])
        dp[i][2] = sum(dp[i-3])

    return sum(dp[n])


ip = int(input())

for _ in range(ip):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        ans = check()
        print(ans)
