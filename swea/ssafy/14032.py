def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = list()
    q.append([a, b, 1])
    while q:
        v = q.pop(0)
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < n and 0 <= nv[1] < n and lst[v[0]][v[1]] + 1 == lst[nv[0]][nv[1]]:
                q.append(nv)
    return v[2]


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    ans = 0
    now = 0
    for i in range(n):
        for j in range(n):
            d = bfs(i, j)
            if d > ans:
                ans = d
                now = lst[i][j]
            elif d == ans:
                if lst[i][j] < now:
                    now = lst[i][j]
    print(f'#{case} {now} {ans}')
