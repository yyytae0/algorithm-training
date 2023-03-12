def bfs(r, c):
    way = {1: [[1, 0], [-1, 0], [0, 1], [0, -1]], 2: [[1, 0], [-1, 0]], 3: [[0, 1], [0, -1]],
           4: [[-1, 0], [0, 1]], 5: [[0, 1], [1, 0]], 6: [[1, 0], [0, -1]], 7: [[0, -1], [-1, 0]]}
    check = {(1, 0): [1, 2, 4, 7], (-1, 0): [1, 2, 5, 6], (0, 1): [1, 3, 6, 7], (0, -1): [1, 3, 4, 5]}
    q = list()
    q.append([r, c, 1])
    visit[r][c] = 1
    cnt = 1
    while q:
        v = q.pop(0)
        for i in way[lst[v[0]][v[1]]]:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] in check[(i[0], i[1])]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if nv[2] > l:
                    return cnt
                cnt += 1
    return cnt


ip = int(input())

for case in range(1, ip+1):
    n, m, r, c, l = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    visit = [[0 for _ in range(m)] for _ in range(n)]
    ans = bfs(r, c)
    print(f'#{case} {ans}')
