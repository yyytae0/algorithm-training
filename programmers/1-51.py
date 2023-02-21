def solution(n):
    answer = -1
    if n == int(n**(1/2))**2:
        answer = (int(n**(1/2))+1)**2
    return answer