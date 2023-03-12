def change(a):
    ans = ''
    stack = list()
    for i in a:
        if i.isalnum():
            ans += i
        elif i == ')':
            while stack:
                d = stack.pop()
                if d == '(':
                    break
                ans += d
        elif i == '*':
            if stack:
                if stack[-1] == '*':
                    ans += stack.pop()
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == '+':
            while stack:
                d = stack.pop()
                if d == '(':
                    stack.append(d)
                    break
                ans += d
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
            a = stack.pop()
            b = stack.pop()
            if i == '*':
                stack.append(a*b)
            elif i == '+':
                stack.append(a+b)
    return stack.pop()


for case in range(1, 11):
    n = int(input())
    a = input()
    ch_a = change(a)
    ans = calc(ch_a)
    print(f'#{case} {ans}')
