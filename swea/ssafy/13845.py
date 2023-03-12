def fight(a, b):
    if lst[a] == 1:
        if lst[b] == 1:
            return a
        elif lst[b] == 2:
            return b
        else:
            return a
    elif lst[a] == 2:
        if lst[b] == 1:
            return a
        elif lst[b] == 2:
            return a
        else:
            return b
    else:
        if lst[b] == 1:
            return b
        elif lst[b] == 2:
            return a
        else:
            return a


def check(s, g):
    if g-s == 1:
        return fight(s, g)
    elif s == g:
        return s

    return fight(check(s, (s+g)//2), check((s+g)//2+1, g))


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = check(0, n-1)
    print(f'#{case} {ans+1}')
