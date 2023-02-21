def solution(s):
    answer = []
    dct = dict()
    for idx, i in enumerate(s):
        if i in dct:
            answer.append(idx - dct[i])
            dct[i] = idx
        else:
            answer.append(-1)
            dct[i] = idx
    return answer
