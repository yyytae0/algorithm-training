def solution(citations):
    answer = 0
    dp = [0 for _ in range(10001)]
    for i in citations:
        dp[i] += 1
    for i in range(9999, -1, -1):
        dp[i] += dp[i+1]
        if dp[i] >= i:
            return i
    return answer