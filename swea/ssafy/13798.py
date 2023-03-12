def check(a):
    stack = list()
    cnt = 0
    for i in a:
        if i == '{' or i == '(':
            stack.append(i)
            cnt += 1
        elif i == '}':
            if cnt == 0:
                return 0
            dummy = stack.pop()
            cnt -= 1
            if dummy != '{':
                return 0
        elif i == ')':
            if cnt == 0:
                return 0
            dummy = stack.pop()
            cnt -= 1
            if dummy != '(':
                return 0
    if cnt:
        return 0
    return 1


ip = int(input())

for case in range(1, ip + 1):
    target = input()
    ans = check(target)
    print(f'#{case} {ans}')
