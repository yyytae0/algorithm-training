def solution(x):
    answer = True
    d = x
    dummy = 0
    while d:
        dummy += d % 10
        d = d//10
    if x % dummy:
        answer = False
    return answer
