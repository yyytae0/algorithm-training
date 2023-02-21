def solution(n):
    answer = 0
    d3 = ''
    while n:
        d3 = str(n % 3) + d3
        n = n//3
    for idx, i in enumerate(d3):
        answer += int(i)*(3**idx)
    return answer
