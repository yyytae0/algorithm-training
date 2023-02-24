from collections import Counter


def solution(k, tangerine):
    c = Counter(tangerine)
    d = c.most_common()
    answer = 0
    for i in d:
        answer += 1
        k -= i[1]
        if k <= 0:
            return answer
    return answer