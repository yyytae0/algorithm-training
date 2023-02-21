def solution(dartResult):
    now = 0
    stack = list()
    dummy = 0
    for i in dartResult:
        if i.isdigit():
            if i == '0' and dummy == '1':
                now = 10
            else:
                stack.append(now)
                now = int(i)
        elif i == 'D':
            now = now**2
        elif i == 'T':
            now = now**3
        elif i == '#':
            now = -now
        elif i == '*':
            now = now*2
            stack[-1] = stack[-1] * 2
        dummy = i
    answer = sum(stack) + now
    return answer