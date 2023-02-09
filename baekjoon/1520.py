import sys


def dfs(a, b):
    global cnt

    if [a, b] == [m - 1, n - 1]:
        return 1

    if dp[a][b] != -1:
        return dp[a][b]

    cnt = 0
    for i in way:
        n_a, n_b = a + i[0], b + i[1]
        if 0 <= n_a <= m-1 and 0 <= n_b <= n-1 and lst[a][b] > lst[n_a][n_b]:
            cnt += dfs(n_a, n_b)
    dp[a][b] = cnt
    return dp[a][b]


sys.setrecursionlimit(10**8)
m, n = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(m))
dp = [[-1 for _ in range(n)] for _ in range(m)]
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = dfs(0, 0)
print(ans)
