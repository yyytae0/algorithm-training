def solution(s):
    n = len(s)
    if n % 2:
        answer = s[n//2]
    else:
        answer = s[n//2-1:n//2+1]
    return answer