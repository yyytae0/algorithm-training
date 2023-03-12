for case in range(1, 11):
    n = int(input())
    lst = list(input())
    stack = list()
    for i in range(0, n, 2):
        stack.append(int(lst[i]))

    for i in range(n//2):
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)

    ans = stack.pop()
    print(f'#{case} {ans}')
