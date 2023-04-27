from collections import deque


def bfs(cnt):
    q = deque()
    q.append([0, 0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m and not visit[nv[0]][nv[1]]:
                if -cnt < lst[nv[0]][nv[1]] <= 0:
                    visit[nv[0]][nv[1]] = 1
                    q.append(nv)
                elif lst[nv[0]][nv[1]] == 1:
                    lst[nv[0]][nv[1]] = -cnt
                    visit[nv[0]][nv[1]] = 1


def check():
    cnt = 0
    for i in lst:
        for j in i:
            if j == 1:
                cnt += 1
    return cnt


way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
cnt = 1
d = check()
while True:
    bfs(cnt)
    now = check()
    if now == 0:
        print(cnt)
        print(d)
        break
    d = now
    cnt += 1
