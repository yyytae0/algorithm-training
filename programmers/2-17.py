def solution(k, ranges):
    answer = []
    dp = []
    n = 1
    dp.append(k)
    while k != 1:
        if not k % 2:
            k = k//2
        else:
            k = k*3 + 1
        dp.append(k + dp[-1])
        n += 1
    for i in ranges:
        if 1 - i[1] > n or i[0] > n-1:
            answer.append(-1)
        else:
            d = dp[i[1] - 1] - dp[i[0]]
            if d < 0:
                answer.append(-1)
            elif d == 0:
                answer.append(0)
            else:
                if i[0]:
                    d1 = dp[i[0]] - dp[i[0] - 1]
                else:
                    d1 = dp[i[0]]
                d2 = dp[i[1] - 1] - dp[i[1] - 2]
                d = d + d1 / 2 - d2 / 2
                answer.append(d)
    return answer


print(solution(1, [[0,0],[0,-1],[2,-3],[3,-3]]))