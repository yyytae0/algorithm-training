def solution(N, stages):
    answer = []
    dct = dict()
    for i in range(1, N+1):
        dct[i] = [0, 0]
    for i in stages:
        for j in range(1, i):
            dct[j][1] += 1
        if i != N+1:
            dct[i][0] += 1
            dct[i][1] += 1
    dummy = []
    for i in range(1, N+1):
        if dct[i][1] == 0 or dct[i][0] == 0:
            dummy.append([0, i])
        else:
            dummy.append([-(dct[i][0]/dct[i][1]), i])
    dummy.sort()
    for i in dummy:
        answer.append(i[1])
    return answer
