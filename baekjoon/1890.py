import sys


def dfs(a, b):
    if [a, b] == [n-1, n-1]:
        return 1

    if dp[a][b] != -1:
        return dp[a][b]

    cnt = 0
    for i in way:
        n_a = a + i[0]*lst[a][b]
        n_b = b + i[1]*lst[a][b]
        if n_a <= n-1 and n_b <= n-1:
            cnt += dfs(n_a, n_b)
    dp[a][b] = cnt
    return dp[a][b]


sys.setrecursionlimit(10**8)
n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
dp = [[-1 for _ in range(n)] for _ in range(n)]
way = [[0, 1], [1, 0]]
ans = dfs(0, 0)
print(ans)
