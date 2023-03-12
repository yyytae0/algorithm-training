def bfs():
    ans = [1]
    q = list()
    q.append(1)
    visit[1] = 1
    while q:
        v = q[0]
        del q[0]
        for i in range(1, a+1):
            if not visit[i] and lst[v][i]:
                q.append(i)
                visit[i] = 1
                ans.append(i)
    return ans


ip = int(input())

for case in range(1, ip+1):
    a, b = map(int, input().split())
    lst = [[0 for _ in range(a+1)] for _ in range(a+1)]
    visit = [0 for _ in range(a+1)]
    for i in range(b):
        x, y = map(int, input().split())
        lst[x][y] = 1
        lst[y][x] = 1
    ans = bfs()
    print(f'#{case}', *ans)
