def solution(number):
    answer = 0
    n = len(number)
    dummy = 0
    for i in range(n):
        dummy += number[i]
        for j in range(i+1, n):
            dummy += number[j]
            for k in range(j+1, n):
                dummy += number[k]
                if not dummy:
                    answer += 1
                dummy -= number[k]
            dummy -= number[j]
        dummy -= number[i]
    return answer
