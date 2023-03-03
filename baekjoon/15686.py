from collections import deque


def bfs():
    q = deque(dummy[:])
    ans = 0
    visit = [[0 for _ in range(n)] for _ in range(n)]
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1], v[2] + 1]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= n-1 and not visit[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                if lst[nv[0]][nv[1]] == 1:
                    ans += v[2] + 1
    return ans


def chick():
    chicken = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 2:
                chicken.append([i, j])
                cnt += 1
    return cnt, chicken


def check(a, c):
    global mn
    if c == m:
        d = bfs()
        if d < mn:
            mn = d
        return

    for i in range(a+1, cnt):
        dummy.append([chicken[i][0], chicken[i][1], 0])
        check(i, c+1)
        dummy.pop()


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
mn = 4000000
dummy = []
cnt, chicken = chick()
check(-1, 0)

print(mn)
