def dfs(a, b):
    if a == n-1 and b == n-1:
        return lst[a][b]

    if dp[a][b] > -1:
        return dp[a][b]

    for i in dp:
        print(*i)

    for i in way:
        na = a+i[0]
        nb = b+i[1]
        if 0 <= na < n and 0 <= nb < n and not visit[na][nb]:
            visit[na][nb] = 1
            if dp[a][b] != -1:
                dp[a][b] = min(dp[a][b], dfs(na, nb) + lst[a][b])
            else:
                dp[a][b] = dfs(na, nb) + lst[a][b]
            visit[na][nb] = 0
    return dp[a][b]


ip = int(input())
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(n))
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dp[n-1][n-1] = 0
    visit[0][0] = 1
    dfs(0, 0)
    for i in dp:
        print(*i)
    print(dp[0][0])
