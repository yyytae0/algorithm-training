def dfs():
    if not stack:
        return
    a = stack.pop()
    ans.append(a)
    for i in range(1, v+1):
        if lst[a][i] and not visit[i]:
            stack.append(i)
            visit[i] = 1
            dfs()


ip = int(input())

for case in range(1, ip+1):
    v, e = map(int, input().split())
    lst = [[0 for _ in range(v+1)] for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    stack = list()
    ans = list()
    for i in range(e):
        x, y = map(int, input().split())
        lst[x][y] = 1
        lst[y][x] = 1

    visit[1] = 1
    stack.append(1)
    dfs()
    print(f'#{case}', *ans)
