def make():
    ans = ''
    stack = list()
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

    return ans


def calc(a):
    stack = list()
    for i in a:
        if i.isalnum():
            stack.append(int(i))
        else:
            if stack:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '*':
                    stack.append(a * b)
    return stack[-1]


for case in range(1, 11):
    n = int(input())
    lst = list(input())
    change = make()
    ans = calc(change)
    print(f'#{case} {ans}')
