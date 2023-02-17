def check(a, b):
    lst = [[0 for _ in range(b)] for _ in range(a)]
    for i in range(a):
        lst[i][0] = 1
    for i in range(b):
        lst[0][i] = 1
    for i in range(1, a):
        for j in range(1, b):
            lst[i][j] = lst[i-1][j] + lst[i][j-1]
    return lst[a-1][b-1]


n, m, k = map(int, input().split())
if not k:
    ans = check(n, m)
else:
    n1 = k//m + 1
    m1 = k%m
    n2 = n - n1 + 1
    m2 = m - m1 + 1
    ans = check(n1, m1) * check(n2, m2)
print(ans)
