def solution(id_list, report, k):
    answer = []
    dct = dict()
    for i in id_list:
        dct[i] = [0, 0]
    for i in report:
        a, b = i.split()
        if a in dct[b]:
            continue
        else:
            dct[b].append(a)
            dct[b][0] += 1
    for i in dct:
        if dct[i][0] >= k:
            for j in range(dct[i][0]):
                dct[dct[i][2+j]][1] += 1
    for i in dct:
        answer.append(dct[i][1])
    return answer
