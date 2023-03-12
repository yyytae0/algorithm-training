ip = int(input())

for case in range(1, ip+1):
    lst = list(input())
    stack = list()
    ans = ''
    for i in lst:
        if i.isalnum():
            ans += i
        else:
            if stack:
                if i == '+' or i == '-':
                    while stack:
                        ans += stack.pop()
                elif i == '*' or i == '/':
                    if stack[-1] == '*' or stack[-1] == '/':
                        ans += stack.pop()
            stack.append(i)
    while stack:
        ans += stack.pop()

    print(f'#{case} {ans}')
