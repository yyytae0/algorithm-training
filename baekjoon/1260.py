def dfs(v):
    global ans
    global visit
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and link[v][i] == 1:
            ans.append(i)
            visit[i] = 1
            dfs(i)


def bfs(v):
    global ans
    global visit
    queue = [v]
    visit[v] = 1
    while queue:
        v = queue[0]
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 0 and link[v][i] == 1:
                ans.append(i)
                queue.append(i)
                visit[i] = 1


n, m, v = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(m))
link = [[0 for _ in range(n+1)] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in lst:
    link[i[0]][i[1]] = 1
    link[i[1]][i[0]] = 1

ans = [v]
dfs(v)
print(*ans)
visit = [0 for _ in range(n+1)]
ans = [v]
bfs(v)
print(*ans)
