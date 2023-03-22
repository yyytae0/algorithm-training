from collections import deque


def bfs():
    way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visit[0][0] = 1
    dct = dict()
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and lst[nv[0]][nv[1]] == 1:
                if dct.get((nv[0], nv[1])):
                    dct[(nv[0], nv[1])] += 1
                else:
                    dct[(nv[0], nv[1])] = 1
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]] and not lst[nv[0]][nv[1]]:
                visit[nv[0]][nv[1]] = 1
                q.append(nv)
    cnt = 0
    for key in dct:
        if dct[key] > 1:
            cnt += 1
            lst[key[0]][key[1]] = 0
    return cnt


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
dummy = 1
cnt = 0
while dummy:
    dummy = bfs()
    cnt += 1
print(cnt-1)
