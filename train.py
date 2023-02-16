def check(a, b, c):
    dummy = list()
    for i in range(a+1, n+1):
        if lst[i][b] == c or not lst[i][b]:
            break
        else:
            dummy.append([i, b])
    for i in range(a-1, 0, -1):
        if lst[i][b] == c or not lst[i][b]:
            break
        else:
            dummy.append([i, b])
    for i in range(b+1, n+1):
        if lst[a][i] == c or not lst[a][i]:
            break
        else:
            dummy.append([a, i])
    for i in range(b-1, 0, -1):
        if lst[a][i] == c or not lst[a][i]:
            break
        else:
            dummy.append([a, i])
    for i in range(1, min(a, b)):
        if lst[a - i][b - i] == c or not lst[a - i][b - i]:
            break
        else:
            dummy.append([a - i, b - i])
    for i in range(1, n - max(a, b)):
        if lst[a + i][b + i] == c or not lst[a + i][b + i]:
            break
        else:
            dummy.append([a + i, b + i])






ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    play = list(list(map(int, input().split())) for _ in range(m))
    lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
    lst[n//2][n//2] = 2
    lst[n//2+1][n//2] = 1      # W = 2, B = 1
    lst[n//2][n//2+1] = 1
    lst[n//2+1][n//2+1] = 2
    for i in play:
