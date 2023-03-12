def solv(a, b):
    d = lst[a][b]
    for i in range(1, lst[a][b]+1):
        for j in [[i, 0], [-i, 0], [0, i], [0, -i]]:
            nv = [a+j[0], b+j[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m:
                d += lst[nv[0]][nv[1]]
    return d


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    ans = 0
    for i in range(n):
        for j in range(m):
            d = solv(i, j)
            if d > ans:
                ans = d
    print(f'#{case} {ans}')