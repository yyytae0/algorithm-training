def check(s, cnt):
    mx = [0, 0]
    if cnt == 0:
        ans = ''
        for i in range(n):
            ans += str(a[i])
        return int(ans)

    if len(a) == 2:
        pass
    for i in range(s+1, n):
        if a[i] >= mx[0]:
            mx = [a[i], i]
    a[s], a[mx[1]] = a[mx[1]], a[s]
    return check(s+1, cnt-1)


ip = int(input())

for case in range(1, ip+1):
    a, k = map(str, input().split())
    n = len(a)
    a = list(map(int, a))
    print(check(0, int(k)))
