def solution(sizes):
    answer = 0
    mn, mx = 0, 0
    for i in sizes:
        if min(i) > mn:
            mn = min(i)
        if max(i) > mx:
            mx = max(i)
    answer = mn * mx
    return answer
