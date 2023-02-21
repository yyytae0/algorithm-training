def solution(k, score):
    answer = []
    lst = list()
    cnt = 0
    for i in score:
        if cnt < k:
            lst.append(i)
            lst.sort()
            cnt += 1
        else:
            if i > lst[0]:
                lst[0] = i
                lst.sort()
        answer.append(lst[0])
    return answer