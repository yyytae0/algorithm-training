def solution(ingredient):
    answer = 0
    stack = list()
    cnt = 0
    for i in ingredient:
        stack.append(i)
        cnt += 1
        if cnt >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
                cnt -= 4
    return answer
