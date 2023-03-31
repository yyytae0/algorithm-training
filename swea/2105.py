def check(a, b):
    for i in range(1, n):
        for j in range(1, n):
            v = [0 for _ in range(101)]
            solv(a, b, i, j, v)


def solv(a, b, c, d, v):
    global ans
    if 2*c+2*d <= ans:
        return
    cnt = 0
    for i in range(c):
        a -= 1
        b += 1
        if 0 <= a < n and 0 <= b < n and not v[lst[a][b]]:
            cnt += 1
            v[lst[a][b]] = 1
        else:
            return
    for i in range(d):
        a += 1
        b += 1
        if 0 <= a < n and 0 <= b < n and not v[lst[a][b]]:
            cnt += 1
            v[lst[a][b]] = 1
        else:
            return
    for i in range(c):
        a += 1
        b -= 1
        if 0 <= a < n and 0 <= b < n and not v[lst[a][b]]:
            cnt += 1
            v[lst[a][b]] = 1
        else:
            return
    for i in range(d):
        a -= 1
        b -= 1
        if 0 <= a < n and 0 <= b < n and not v[lst[a][b]]:
            cnt += 1
            v[lst[a][b]] = 1
        else:
            return
    if cnt and cnt > ans:
        ans = cnt


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    ans = -1
    for i in range(n):
        for j in range(n):
            check(i, j)
    print(f'#{case} {ans}')
