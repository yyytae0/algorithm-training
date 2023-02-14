ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    dp = [1 for _ in range((n//10)+1)]
    for i in range(2, (n//10)+1):
        dp[i] = dp[i-1] + 2*dp[i-2]
    print(f'#{case}', dp[n//10])
