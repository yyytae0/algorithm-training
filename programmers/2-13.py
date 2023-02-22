def solution(k, d):
    dp = [0 for _ in range(1000001)]
    for i in range(0, d+1, k):
        dp[i] += 1
    for i in range(1, 1000001):
        dp[i] += dp[i-1]
    answer = 0
    for i in range(0, d+1, k):
        answer += dp[int((d**2 - i**2)**(1/2))]
    return answer
