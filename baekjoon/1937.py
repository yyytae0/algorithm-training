from sys import setrecursionlimit


def dfs(a, b):
    if dp[a][b]:
        return dp[a][b]
    dummy = 0
    for i in way:
        nv = [a+i[0], b+i[1]]
        if 0 <= nv[0] < n and 0 <= nv[1] < n and lst[nv[0]][nv[1]] > lst[a][b]:
            dp[a][b] = max(dp[a][b], dfs(nv[0], nv[1])+1)
            dummy = 1
    if dummy:
        return dp[a][b]
    else:
        dp[a][b] = 1
        return 1


setrecursionlimit(10**6)
n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
dp = [[0 for _ in range(n)] for _ in range(n)]
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0
for i in range(n):
    for j in range(n):
        d = dfs(i, j)
        ans = max(d, ans)
print(ans)
