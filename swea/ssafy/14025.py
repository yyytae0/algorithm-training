def check(a):
    if not dct[a].isdigit():
        if dct[a] == '*':
            return check(left[a]) * check(right[a])
        elif dct[a] == '+':
            return check(left[a]) + check(right[a])
        elif dct[a] == '-':
            return check(left[a]) - check(right[a])
        elif dct[a] == '/':
            return check(left[a]) / check(right[a])

    else:
        return int(dct[a])


for case in range(1, 11):
    n = int(input())
    left = [0 for _ in range(n + 1)]
    right = [0 for _ in range(n + 1)]
    dct = dict()
    for i in range(n):
        lst = list(input().split())
        a = int(lst.pop(0))
        b = lst.pop(0)
        if lst:
            left[a] = int(lst.pop(0))
        if lst:
            right[a] = int(lst.pop(0))
        dct[a] = b

    print(f'#{case} {int(check(1))}')

