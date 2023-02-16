n1, m1 = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n1))
n2, m2 = map(int, input().split())
b = list(list(map(int, input().split())) for _ in range(n2))
lst = [[0 for _ in range(m2)] for _ in range(n1)]
for i in range(n1):
    for j in range(m2):
        ans = 0
        for k in range(m1):
            ans = ans + a[i][k] * b[k][j]
        lst[i][j] = ans
for i in lst:
    print(*i)
