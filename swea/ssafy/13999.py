def cross(a, b):
    cnt = lst[a][b]
    for i in range(1, m):
        for j in [[a, b+i], [a, b-i], [a+i, b], [a-i, b]]:
            if 0 <= j[0] < n and 0 <= j[1] < n:
                cnt += lst[j[0]][j[1]]
    return cnt


def diag(a, b):
    cnt = lst[a][b]
    for i in range(1, m):
        for j in [[a+i, b+i], [a+i, b-i], [a-i, b+i], [a-i, b-i]]:
            if 0 <= j[0] < n and 0 <= j[1] < n:
                cnt += lst[j[0]][j[1]]
    return cnt


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    mx = 0
    for i in range(n):
        for j in range(n):
            c = cross(i, j)
            d = diag(i, j)
            if max(c, d) > mx:
                mx = max(c, d)
    print(f'#{case} {mx}')
