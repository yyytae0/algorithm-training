from collections import deque


def bfs():
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([0, 0, 1, 1])
    visit[0][0] = 1
    visit1[0][0] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1, v[3]]
            if v[3]:
                if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]]:
                    if lst[nv[0]][nv[1]] == 1:
                        if v[3]:
                            nv[3] = 0
                    q.append(nv)
                    visit[nv[0]][nv[1]] = 1
                    visit1[nv[0]][nv[1]] = 1
                    if [nv[0], nv[1]] == [n - 1, m - 1]:
                        return nv[2]
            else:
                if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit1[nv[0]][nv[1]] and lst[nv[0]][nv[1]] != 1:
                    q.append(nv)
                    visit1[nv[0]][nv[1]] = 1
                    if [nv[0], nv[1]] == [n-1, m-1]:
                        return nv[2]
    return -1


n, m = map(int, input().split())
lst = list(list(map(int, input())) for _ in range(n))
if [n, m] == [1, 1]:
    print(1)
else:
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit1 = [[0 for _ in range(m)] for _ in range(n)]
    print(bfs())

# 97% 틀림
