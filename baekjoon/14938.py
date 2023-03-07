def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


n, m, r = map(int, input().split())
lst = list(map(int, input().split()))
d = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(r):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
floyd_warshall()
ans = 0
for i in range(n):
    dummy = 0
    for j in range(n):
        if d[i][j] <= m:
            dummy += lst[j]
    if ans < dummy:
        ans = dummy
print(ans)
