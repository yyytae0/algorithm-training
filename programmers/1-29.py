def solution(left, right):
    answer = 0
    double = [0 for _ in range(1001)]
    for i in range(1, 33):
        if i**2 <= 1000:
            double[i**2] = 1
    for i in range(left, right+1):
        if double[i]:
            answer -= i
        else:
            answer += i
    return answer
