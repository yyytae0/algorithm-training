import sys


def dfs(a, cnt):
    if dp[a[0]][a[1]] > cnt:
        dp[a[0]][a[1]] = cnt
    if a == [n-1, n-1]:
        return
    for i in way:
        nv = [a[0]+i[0], a[1]+i[1]]
        if 0 <= nv[0] < n and 0 <= nv[1] < n and not visit[nv[0]][nv[1]]:
            if not lst[nv[0]][nv[1]]:
                if dp[nv[0]][nv[1]] > cnt+1:
                    visit[nv[0]][nv[1]] = 1
                    dfs(nv, cnt+1)
                    visit[nv[0]][nv[1]] = 0
            else:
                if dp[nv[0]][nv[1]] > cnt:
                    visit[nv[0]][nv[1]] = 1
                    dfs(nv, cnt)
                    visit[nv[0]][nv[1]] = 0


sys.setrecursionlimit(10**6)
n = int(input())
lst = list(list(map(int, input())) for _ in range(n))
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dp = [[2500 for _ in range(n)] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
visit[0][0] = 1
dfs([0, 0], 0)
# for i in dp:
#     print(*i)
print(dp[n-1][n-1])
