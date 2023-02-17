def multi(a, b):
    d = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[i][j] = (d[i][j] + ((a[i][k]%1000) * (b[k][j]%1000)) % 1000) % 1000
    return d


def solve(a, b):
    d = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[i][j] = (d[i][j] + ((a[i][k]%1000) * (a[k][j]%1000)) % 1000) % 1000

    if b == 2:
        return d
    if b == 1:
        return a
    if b % 2:
        return multi(solve(d, b//2), a)
    else:
        return solve(d, b//2)


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
ans = solve(lst, m)
for i in ans:
    for j in i:
        print(j%1000, end=' ')
    print()
