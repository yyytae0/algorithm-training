from collections import deque


def bfs(a):
    q = deque()
    q.append([a, 1])
    visit[a] = 1
    while q:
        v = q.popleft()
        for i in [v[0]*2, v[0]*10 + 1]:
            if i < b+1:
                if i not in visit.keys():
                    q.append([i, v[1]+1])
                    visit[i] = 1
                    if i == b:
                        return v[1] + 1

    return -1


a, b = map(int, input().split())
visit = dict()
print(bfs(a))
