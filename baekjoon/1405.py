def dfs(cnt, now):
    global ans
    if cnt == 0:
        ans += now[0]
        return

    for i in go:
        nv = [now[0]*(i[2]/100), now[1]+i[0], now[2]+i[1]]
        if i[2] != 0 and not visit[nv[1]][nv[2]]:
            visit[nv[1]][nv[2]] = 1
            dfs(cnt-1, nv)
            visit[nv[1]][nv[2]] = 0


n, a, b, c, d = map(int, input().split())
go = [[0, 1, a], [0, -1, b], [-1, 0, c], [1, 0, d]]
visit = [[0 for _ in range(30)] for _ in range(30)]
g = [1, 15, 15]
visit[15][15] = 1
ans = 0.0
dfs(n, g)
print(ans)