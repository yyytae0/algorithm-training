from sys import stdin


def check(a, b):
    global ans
    if b+4 <= m:
        ans = max(lst[a][b] + lst[a][b+1] + lst[a][b+2] + lst[a][b+3], ans)
    if a+4 <= n:
        ans = max(lst[a][b] + lst[a+1][b] + lst[a+2][b] + lst[a+3][b], ans)
    if b+2 <= m and a+2 <= n:
        ans = max(lst[a][b] + lst[a + 1][b] + lst[a][b+1] + lst[a+1][b+1], ans)
    if b+2 <= m and a+3 <= n:
        ans = max(lst[a][b] + lst[a+1][b] + lst[a+2][b] + lst[a+2][b+1],
                  lst[a][b] + lst[a][b+1] + lst[a+1][b+1] + lst[a+2][b+1],
                  lst[a][b] + lst[a+1][b] + lst[a+2][b] + lst[a][b+1],
                  lst[a][b+1] + lst[a+1][b+1] + lst[a+2][b+1] + lst[a+2][b],
                  lst[a][b+1] + lst[a+1][b+1] + lst[a+2][b+1] + lst[a+1][b],
                  lst[a][b] + lst[a+1][b] + lst[a+2][b] + lst[a+1][b+1],
                  lst[a][b] + lst[a+1][b] + lst[a+1][b+1] + lst[a+2][b+1],
                  lst[a][b+1] + lst[a+1][b+1] + lst[a+1][b] + lst[a+2][b],
                  ans)
    if b+3 <= m and a+2 <= n:
        ans = max(lst[a][b] + lst[a+1][b] + lst[a+1][b+1] + lst[a+1][b+1],
                  lst[a][b] + lst[a][b+1] + lst[a][b+2] + lst[a+1][b+2],
                  lst[a][b] + lst[a+1][b] + lst[a][b+1] + lst[a][b+2],
                  lst[a+1][b] + lst[a+1][b+1] + lst[a+1][b+2] + lst[a][b+2],
                  lst[a][b] + lst[a+1][b+1] + lst[a][b+1] + lst[a][b+2],
                  lst[a][b+1] + lst[a+1][b] + lst[a+1][b+1] + lst[a+1][b+2],
                  lst[a][b] + lst[a][b+1] + lst[a+1][b+1] + lst[a+1][b + 2],
                  lst[a+1][b] + lst[a+1][b+1] + lst[a][b+1] + lst[a][b + 2],
                  ans)


n, m = map(int, stdin.readline().split())
lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
ans = 0
for i in range(n):
    for j in range(m):
        check(i, j)
print(ans)
