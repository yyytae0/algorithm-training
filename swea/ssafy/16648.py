def check():
    for i in range(1, 99):
        for j in range(1, 99):
            if lst[i][j] == 2:
                return bfs(i, j)


def bfs(i, j):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = list()
    q.append([i, j])
    lst[i][j] = 1
    while q:
        v = q.pop(0)
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if lst[nv[0]][nv[1]] != 1:
                q.append(nv)
                if lst[nv[0]][nv[1]] == 3:
                    return 1
                lst[nv[0]][nv[1]] = 1
    return 0


for _ in range(10):
    case = int(input())
    lst = list(list(map(int, input())) for _ in range(100))
    print(f'#{case} {check()}')
