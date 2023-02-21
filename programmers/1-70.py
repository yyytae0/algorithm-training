def solution(a, b):
    weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    a1 = [1, 3, 5, 7, 8, 10, 12]
    a2 = [4, 6, 9, 11]
    d = 6
    for i in range(1, a):
        if i in a1:
            d += 31
        elif i in a2:
            d += 30
        elif i == 2:
            d += 29
    d += b - 2
    answer = weekday[d % 7]
    return answer


print(solution(5, 24))