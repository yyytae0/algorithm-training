def solution(X, Y):
    answer = ''
    dct1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    dct2 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in X:
        dct1[int(i)] += 1
    for i in Y:
        dct2[int(i)] += 1
    for i in range(9, -1, -1):
        if i == 0:
            if answer:
                answer += str(i) * min(dct1[i], dct2[i])
            else:
                if dct1[i] and dct2[i]:
                    answer = '0'
        else:
            answer += str(i) * min(dct1[i], dct2[i])
    if not answer:
        return '-1'
    return answer
