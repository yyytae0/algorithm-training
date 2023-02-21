def solution(t, p):
    answer = 0
    n = len(p)
    p = int(p)
    for i in range(len(t)-n+1):
        if int(t[i:i+n]) <= p:
            answer += 1
    return answer
