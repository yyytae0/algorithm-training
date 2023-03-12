def bfs(s, g):
    q = list()
    q.append([s, 0])
    visit[s] = 1
    while q:
        v = q.pop(0)
        for i in range(1, n+1):
            if lst[v[0]][i] and not visit[i]:
                q.append([i, v[1]+1])
                visit[i] = 1
                if i == g:
                    return v[1] + 1
    return 0


ip = int(input())

for case in range(1, ip+1):
    n, e = map(int, input().split())
    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for i in range(e):
        a, b = map(int, input().split())
        lst[a][b] = 1
        lst[b][a] = 1
    s, g = map(int, input().split())
    ans = bfs(s, g)
    print(f'#{case} {ans}')
