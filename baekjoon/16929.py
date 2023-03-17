from sys import setrecursionlimit


def dfs(a, b, c):
    global cnt, ans
    if ans:
        return
    for i in way:
        na, nb = a+i[0], b+i[1]
        if na == si and nb == sj:
            if cnt >= 3:
                ans = 1
                return
        if 0 <= na < n and 0 <= nb < m and lst[na][nb] == c and not visit[na][nb]:
            visit[na][nb] = 1
            visit2[na][nb] = 1
            cnt += 1
            dfs(na, nb, c)
            cnt -= 1
            visit[na][nb] = 0


setrecursionlimit(10**5)
n, m = map(int, input().split())
lst = list(list(input()) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
visit2 = [[0 for _ in range(m)] for _ in range(n)]
way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0
for si in range(n):
    for sj in range(m):
        if not visit[si][sj] and not ans:
            cnt = 0
            visit[si][sj] = 1
            visit2[si][sj] = 1
            dfs(si, sj, lst[si][sj])
if ans:
    print('Yes')
else:
    print('No')
