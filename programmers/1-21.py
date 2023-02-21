def solution(babbling):
    answer = 0
    lst = ['aya', 'ye', 'woo', 'ma']
    check = ['ayaaya', 'yeye', 'woowoo', 'mama']
    for i in babbling:
        d = i
        for j in check:
            if j in d:
                break
        else:
            for j in lst:
                d = d.replace(j, ' ')
            d = d.replace(' ', '')
            if not d:
                answer += 1
    return answer
