def check(a, b, c):
    dummy = list()
    chk = list()
    for i in range(a+1, n+1):
        if not lst[i][b]:
            break
        if lst[i][b] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([i, b])
    dummy = list()
    for i in range(a-1, 0, -1):
        if not lst[i][b]:
            break
        if lst[i][b] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([i, b])
    dummy = list()
    for i in range(b+1, n+1):
        if not lst[a][i]:
            break
        if lst[a][i] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([a, i])
    dummy = list()
    for i in range(b-1, 0, -1):
        if not lst[a][i]:
            break
        if lst[a][i] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([a, i])
    dummy = list()
    for i in range(1, min(a, b)):
        if not lst[a-i][b-i]:
            break
        if lst[a - i][b - i] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([a - i, b - i])
    dummy = list()
    for i in range(1, n - max(a, b)):
        if not lst[a+i][b+i]:
            break
        if lst[a + i][b + i] == c:
            chk.extend(dummy)
            break
        else:
            dummy.append([a + i, b + i])
    dummy = list()
    for i in range(1, n):
        if 1 <= a+i <= n and 1 <= b-i <= n:
            if not lst[a+i][b-i]:
                break
            if lst[a + i][b - i] == c:
                chk.extend(dummy)
                break
            else:
                dummy.append([a + i, b - i])
    dummy = list()
    for i in range(1, n):
        if 1 <= a - i <= n and 1 <= b + i <= n:
            if not lst[a - i][b + i]:
                break
            if lst[a - i][b + i] == c:
                chk.extend(dummy)
                break
            else:
                dummy.append([a - i, b + i])
    lst[a][b] = c
    for i in chk:
        lst[i[0]][i[1]] = c


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
        check(i[0], i[1], i[2])

    cnt1 = 0
    cnt2 = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if lst[i][j] == 1:
                cnt1 += 1
            elif lst[i][j] == 2:
                cnt2 += 1

    print(f'#{case}', cnt1, cnt2)
