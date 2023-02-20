def solution(n, lost, reserve):
    answer = 0
    dct = dict()
    for i in range(1, n+1):
        dct[i] = 1
    for i in lost:
        dct[i] -= 1
    reserve.sort()
    for idx, i in enumerate(reserve):
        if not dct[i]:
            dct[i] += 1
            reserve[idx] = 0
    for i in reserve:
        if i == 0:
            continue
        if dct[i]:
            if i == 1:
                if dct[i+1] == 0:
                    dct[i+1] += 1
            elif i == n:
                if dct[i-1] == 0:
                    dct[i-1] += 1
            else:
                if dct[i-1] == 0:
                    dct[i-1] += 1
                elif dct[i+1] == 0:
                    dct[i+1] += 1
    for i in dct:
        answer += dct[i]

    return answer
