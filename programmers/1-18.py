def solution(k, m, score):
    answer = 0
    dct = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in score:
        dct[i] += 1
    for i in range(9, 0, -1):
        answer += i*(dct[i]//m)*m
        if i > 1:
            dct[i-1] += dct[i] % m
    return answer
