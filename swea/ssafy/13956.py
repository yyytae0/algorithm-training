def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = list()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q[0]
        del q[0]
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= n-1 and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] != 1:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if lst[nv[0]][nv[1]] == 2:
                    return 1
    return 0


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(n))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dummy = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 3:
                dummy = 1
                ans = bfs(i, j)
                print(f'#{case} {ans}')
                break
        if dummy:
            break
