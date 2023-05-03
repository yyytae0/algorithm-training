from collections import deque


def bfs():
    q = deque()
    q.append([0, 0, k, 0])
    visit[0][0] = 1
    while q:
        v = q.popleft()
        for i in way1:
            nv = [v[0]+i[0], v[1]+i[1], v[2], v[3]+1]
            if 0 <= nv[0] < h and 0 <= nv[1] < w and not visit[nv[0]][nv[1]] and not lst[nv[0]][nv[1]]:
                visit[nv[0]][nv[1]] = 1
                q.append(nv)
                if nv[0] == h-1 and nv[1] == w-1:
                    return nv[3]
        if v[2] > 0:
            for i in way2:
                nv = [v[0] + i[0], v[1] + i[1], v[2]-1, v[3] + 1]
                if 0 <= nv[0] < h and 0 <= nv[1] < w and not visit[nv[0]][nv[1]] and not lst[nv[0]][nv[1]]:
                    visit[nv[0]][nv[1]] = 1
                    q.append(nv)
                    if nv[0] == h - 1 and nv[1] == w - 1:
                        return nv[3]
    return -1


way1 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
way2 = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
k = int(input())
w, h = map(int, input().split())
visit = [[0 for _ in range(w)] for _ in range(h)]
lst = list(list(map(int, input().split())) for _ in range(h))
print(bfs())
