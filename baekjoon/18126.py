from collections import deque


def bfs():
    q = deque()
    q.append([1, 0])
    visit[1] = 1
    ans = 0
    while q:
        v = q.popleft()
        if v[1] > ans:
            ans = v[1]
        for i in tree[v[0]]:
            if not visit[i]:
                q.append([i, v[1]+lst[v[0]][i]])
                visit[i] = 1
    return ans


n = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c
    tree[a].append(b)
    tree[b].append(a)
print(bfs())