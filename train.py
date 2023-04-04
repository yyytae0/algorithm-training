def check(a):
    global flag
    if a == 81:
        flag = 1
        return True

    y = a//9
    x = a % 9
    if lst[y][x] != 0:
        return check(a+1)

    for j in range(1, 10):
        if crow[y][j] and ccol[x][j] and ccro[(y // 3) * 3 + (x // 3)][j]:
            crow[y][j] = ccol[x][j] = ccro[(y // 3) * 3 + (x // 3)][j] = 0
            if check(a + 1):
                return True
            crow[y][j] = ccol[x][j] = ccro[(y // 3) * 3 + (x // 3)][j] = 1
    return False


ccro = [[1 for _ in range(10)] for _ in range(10)]
crow = [[1 for _ in range(10)] for _ in range(10)]
ccol = [[1 for _ in range(10)] for _ in range(10)]
lst = [[0 for _ in range(9)] for _ in range(9)]
ans = -1
for i in range(1, 82):
    a, b, c = map(int, input().split())
    sq = (a-1)//3*3 + (b-1)//3
    flag = 0
    if ans > 0:
        continue
    if not crow[a][c] or not ccol[b][c] or not ccro[sq][c]:
        ans = i
        continue
    crow[a][c] = 0
    ccol[b][c] = 0
    ccro[sq][c] = 0
    lst[a-1][b-1] = c
    if i > 20:
        check(0)
        if flag:
            ans = i
print(ans)