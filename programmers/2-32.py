def solution(n):
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[0] = [1, 0]
    dp[1] = [1, 0]
    for i in range(2, n+1):
        dp[i][0] = sum(dp[i-1]) % 1234567
        dp[i][1] = sum(dp[i-2]) % 1234567
    answer = sum(dp[n]) % 1234567
    return answer