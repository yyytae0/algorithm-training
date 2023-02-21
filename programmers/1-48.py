def solution(n, m):
    answer = []
    d1 = max(n, m)
    d2 = min(n, m)
    while d1%d2:
        d1, d2 = d2, d1%d2
    answer.append(d2)
    answer.append(n*m//d2)
    return answer