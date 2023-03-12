def check():
    stack = list()
    for i in lst:
        if i.isalnum():
            stack.append(int(i))
        else:
            if i == '.':
                ans = stack.pop()
                if stack:
                    return 'error'
                else:
                    return ans
            if stack:
                a = stack.pop()
                if stack:
                    b = stack.pop()
                    if i == '+':
                        stack.append(a+b)
                    elif i == '-':
                        stack.append(b-a)
                    elif i == '*':
                        stack.append(a*b)
                    elif i == '/':
                        stack.append(b//a)
                else:
                    return 'error'
            else:
                return 'error'
    return 'error'


ip = int(input())

for case in range(1, ip+1):
    lst = list(input().split())
    ans = check()
    print(f'#{case} {ans}')
