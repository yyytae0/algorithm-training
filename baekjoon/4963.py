from collections import deque


def bfs(a, b):
    way = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= h-1 and 0 <= new_v[1] <= w-1 and not visit[new_v[0]][new_v[1]] and lst[new_v[0]][new_v[1]]:
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1


while True:
    w, h = map(int, input().split())
    if w == 0:
        break

    lst = list(list(map(int, input().split())) for _ in range(h))
    visit = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1 and visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)
