def solution(weights):
    answer = 0
    cnt = [0 for _ in range(4001)]
    cnt1 = [0 for _ in range(1001)]
    n = len(weights)
    for i in range(n):
        d1 = weights[i]
        cnt1[d1] += 1
        for j in [d1 * 2, d1 * 3, d1 * 4]:
            cnt[j] += 1

    for i in range(n):
        d1 = weights[i]
        answer = answer + cnt[d1*2] + cnt[d1*3] + cnt[d1*4] - 2*cnt1[d1] - 1

    return answer//2


print(solution([100, 180, 360, 100, 270]))