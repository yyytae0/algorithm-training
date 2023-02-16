from collections import deque


def bfs():
    way = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    q = deque()
    q.append(shark)
    visit[shark[0]][shark[1]] = 1
    ns = 0
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1], v[2], v[3], v[4]+1]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= n-1 and not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] <= nv[2]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if lst[nv[0]][nv[1]]:
                    if lst[nv[0]][nv[1]] < nv[2]:
                        nv[3] = nv[3] + 1
                        if not ns:
                            ns = nv
                        if nv[3] == nv[2]:
                            nv[2] += 1
                            nv[3] = 0
                        if nv[4] > ns[4]:
                            lst[ns[0]][ns[1]] = 0
                            return ns
                        if nv[0] == ns[0]:
                            if nv[1] <= ns[1]:
                                ns = nv
                        elif nv[0] < ns[0]:
                            ns = nv

    if ns:
        lst[ns[0]][ns[1]] = 0
        return ns
    else:
        return 0


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
f = 0
for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            shark = [i, j, 2, 0, 0]  # [x,y,크기,먹은수,초]
            lst[i][j] = 0
        elif lst[i][j] == 1:
            f += 1
if f:
    while True:
        visit = [[0 for _ in range(n)] for _ in range(n)]
        dummy = bfs()
        if dummy:
            shark = dummy
        else:
            print(shark[4])
            break
else:
    print(0)
