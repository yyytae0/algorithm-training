def solution(a, b):
    n = (max(a, b) - min(a, b)) + 1
    if n % 2:
        answer = (a+b) * (n//2) + min(a, b) + n//2
    else:
        answer = (a+b) * (n//2)
    return answer