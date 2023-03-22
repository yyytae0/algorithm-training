from collections import deque


def fire():
    while fire_q:
        v = fire_q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < h and 0 <= nv[1] < w and not dp[nv[0]][nv[1]]:
                fire_q.append(nv)
                dp[nv[0]][nv[1]] = dp[v[0]][v[1]] + 1


def bfs():
    q = deque()
    q.append(now)
    visit = [[0 for _ in range(w)] for _ in range(h)]
    visit[now[0]][now[1]] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1], v[2]+1]
            if 0 <= nv[0] < h and 0 <= nv[1] < w:
                if (not dp[nv[0]][nv[1]] or dp[nv[0]][nv[1]] > nv[2]) and not visit[nv[0]][nv[1]]:
                    q.append(nv)
                    visit[nv[0]][nv[1]] = 1
            else:
                return v[2]
    return 'IMPOSSIBLE'


ip = int(input())

for case in range(ip):
    w, h = map(int, input().split())
    lst = list(list(input()) for _ in range(h))
    dp = [[0 for _ in range(w)] for _ in range(h)]
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    fire_q = deque()
    for i in range(h):
        for j in range(w):
            if lst[i][j] == '*':
                fire_q.append([i, j])
                dp[i][j] = 1
            elif lst[i][j] == '#':
                dp[i][j] = -1
            elif lst[i][j] == '@':
                now = [i, j, 1]
    fire()
    # for i in dp:
    #     print(*i)
    print(bfs())
