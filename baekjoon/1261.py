from sys import setrecursionlimit


def dfs(a):
    if a == [m-1, n-1]:
        return
    for i in way:
        nv = [a[0]+i[0], a[1]+i[1]]
        if 0 <= nv[0] < m and 0 <= nv[1] < n:
            d = dp[a[0]][a[1]]
            if lst[nv[0]][nv[1]]:
                d += 1
            if dp[nv[0]][nv[1]] > d:
                dp[nv[0]][nv[1]] = d
                dfs(nv)


setrecursionlimit(10**6)
n, m = map(int, input().split())
lst = list(list(map(int, input())) for _ in range(m))
dp = [[float('inf') for _ in range(n)] for _ in range(m)]
dp[0][0] = 0
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
s = [0, 0]
dfs(s)
print(dp[-1][-1])
