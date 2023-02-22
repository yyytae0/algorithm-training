def solution(n, l, r):
    answer = 0
    dp = ['' for _ in range(n+1)]
    dp[0] = '1'
    for i in range(1, n+1):
        dummy = ''
        for j in dp[i-1]:
            if j == '1':
                dummy += '11011'
            elif j == '0':
                dummy += '00000'
        dp[i] = dummy
    for i in range(l-1, r):
        if dp[n][i] == '1':
            answer += 1
    return answer


print(solution(2, 4, 17))