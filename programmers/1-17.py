def solution(number, limit, power):
    answer = 0
    cnt = [0 for _ in range(number+1)]
    for i in range(1, number+1):
        for j in range(1, number+1):
            if i*j <= number:
                cnt[i*j] += 1
            else:
                break
    for i in range(1, number+1):
        if cnt[i] > limit:
            answer += power
        else:
            answer += cnt[i]
    return answer


print(solution(5, 3, 2), 10)
print(solution(10, 3, 2), 21)