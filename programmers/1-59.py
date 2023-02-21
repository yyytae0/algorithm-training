def solution(n):
    answer = ''
    answer += '수박' * (n//2)
    answer += '수' * (n%2)
    return answer