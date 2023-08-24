from collections import deque


def bfs(a, b, cnt):
    q = deque()
    v = [a, b]
    q.append(v)
    while q:
        v = q.popleft()
        if lst[v[0]][v[1]] == 'D':
            nv = [v[0]+1, v[1]]
        elif lst[v[0]][v[1]] == 'L':
            nv = [v[0], v[1]-1]
        elif lst[v[0]][v[1]] == 'R':
            nv = [v[0], v[1]+1]
        else:
            nv = [v[0]-1, v[1]]
        if 0 <= nv[0] < n and 0 <= nv[1] < m:
            if not visit[nv[0]][nv[1]]:
                visit[nv[0]][nv[1]] = cnt
                q.append(nv)
            elif visit[nv[0]][nv[1]] < cnt:
                visit[nv[0]][nv[1]] = cnt
                return 0
            else:
                return 1
    return 1


n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
cnt = 1
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            visit[i][j] = cnt
            ans += bfs(i, j, cnt)
            cnt += 1
print(ans)
