def make():
    for i in range(n):
        for j in range(i+1, n):
            chk.append([i, j])


def check(cnt):
    global ans
    if cnt == 0:
        now = 0
        for i in range(n):
            now += a[-1 - i] * (10 ** i)
        if now > ans:
            ans = now
        return

    for i in chk:
        a[i[0]], a[i[1]] = a[i[1]], a[i[0]]
        if a[0] == mx:
            check(cnt - 1)
        a[i[0]], a[i[1]] = a[i[1]], a[i[0]]


ip = int(input())

for case in range(1, ip+1):
    a, b = map(str, input().split())
    b = int(b)
    a = list(map(int, a))
    n = len(a)
    if n > 2:
        chk = []
        mx = max(a)
        ans = 0
        make()
        check(b)
        print(f'#{case} {ans}')
    else:
        pass
