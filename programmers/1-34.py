def solution(numbers):
    answer = []
    check = [0 for _ in range(201)]
    for idx, i in enumerate(numbers):
        for j in range(idx+1, len(numbers)):
            if not check[i+numbers[j]]:
                check[i+numbers[j]] = 1
                answer.append(i+numbers[j])
    answer.sort()
    return answer