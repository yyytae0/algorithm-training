from collections import deque


def bfs(a):
    q = deque()
    q.append([a, 0])
    visit[a] = 1
    while q:
        v = q.popleft()
        for i in [v[0] + u, v[0] - d]:
            if max(1, min(s - d, g - d)) <= i <= max(s + u + d, g + u + d) and i not in visit.keys():
                q.append([i, v[1]+1])
                visit[i] = 1
                if i == g:
                    return v[1] + 1

    return 'use the stairs'


f, s, g, u, d = map(int, input().split())
visit = dict()
if s == g:
    print(0)

elif s > g and d == 0:
    print('use the stairs')

elif s < g and u == 0:
    print('use the stairs')

else:
    print(bfs(s))
