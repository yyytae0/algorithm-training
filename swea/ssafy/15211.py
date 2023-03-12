def bfs(a, b):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = list()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.pop(0)
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if lst[nv[0]][nv[1]] != 1 and not visit[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if lst[nv[0]][nv[1]] == 3:
                    return 1
    return 0


for case in range(1, 11):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(16))
    visit = [[0 for _ in range(16)] for _ in range(16)]
    ans = bfs(1, 1)
    print(f'#{case} {ans}')
