def solution(today, terms, privacies):
    answer = []
    term = dict()
    tod = [int(today[:4]), int(today[5:7]), int(today[8:10])]
    for i in terms:
        term[i[0]] = int(i[2:])

    cnt = 0
    for i in privacies:
        cnt += 1
        v = i[-1]
        date = [int(i[:4]), int(i[5:7]), int(i[8:10])]
        date[1] = date[1] + term[v]
        while date[1] > 12:
            date[1] -= 12
            date[0] += 1

        for j in range(3):
            if tod[j] < date[j]:
                break
            elif tod[j] > date[j]:
                answer.append(cnt)
                break
        else:
            answer.append(cnt)
    return answer
