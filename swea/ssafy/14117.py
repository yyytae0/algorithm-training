from sys import setrecursionlimit

def dfs(a, b):
    if a == n-1 and b == n-1:
        return

    for i in way:
        na = a+i[0]
        nb = b+i[1]
        if 0 <= na < n and 0 <= nb < n and dp[na][nb] > dp[a][b]+lst[na][nb]:
            dp[na][nb] = dp[a][b] + lst[na][nb]
            dfs(na, nb)


setrecursionlimit(10**6)
ip = int(input())
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(n))
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0] = lst[0][0]
    dfs(0, 0)
    print(dp[n-1][n-1])
