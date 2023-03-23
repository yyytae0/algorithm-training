def dfs(v):
    global ans
    if v[3] > ans:
        ans = v[3]

    for i in way:
        nv = [v[0] + i[0], v[1] + i[1], v[2], v[3] + 1, v[4]]
        if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit[nv[0]][nv[1]]:
            nv[4] = lst[nv[0]][nv[1]]
            visit[nv[0]][nv[1]] = 1
            if nv[4] < v[4]:
                dfs(nv)
            elif not v[2] and nv[4] - k < v[4]:
                nv[2] += 1
                nv[4] = v[4] - 1
                dfs(nv)
                nv[2] -= 1
            visit[nv[0]][nv[1]] = 0


ip = int(input())
way = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for case in range(1, ip+1):
    n, k = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    visit = [[0 for _ in range(n)] for _ in range(n)]
    mx_lst = []
    mx = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] > mx:
                mx = lst[i][j]
                mx_lst = [[i, j, 0, 1, mx]]
            elif lst[i][j] == mx:
                mx_lst.append([i, j, 0, 1, mx])
    ans = 0
    for i in mx_lst:
        visit[i[0]][i[1]] = 1
        dfs(i)
        visit[i[0]][i[1]] = 0
    print(f'#{case} {ans}')
