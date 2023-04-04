def check(a):
    if a == n:
        return True

    i = chk[a]
    for j in range(1, 10):
        if crow[i[0]][j] and ccol[i[1]][j] and ccro[(i[0] // 3) * 3 + (i[1] // 3)][j]:
            crow[i[0]][j] = ccol[i[1]][j] = ccro[(i[0] // 3) * 3 + (i[1] // 3)][j] = 0
            lst[i[0]][i[1]] = j
            if check(a + 1):
                return True
            lst[i[0]][i[1]] = 0
            crow[i[0]][j] = ccol[i[1]][j] = ccro[(i[0] // 3) * 3 + (i[1] // 3)][j] = 1
    return False


lst = list(list(map(int, input())) for _ in range(9))
chk = []
crow = [[1 for _ in range(10)] for _ in range(9)]
ccol = [[1 for _ in range(10)] for _ in range(9)]
ccro = [[1 for _ in range(10)] for _ in range(9)]
n = 0
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            chk.append([i, j])
            n += 1
        else:
            crow[i][lst[i][j]] = 0
            ccol[j][lst[i][j]] = 0
            ccro[(i//3)*3+(j//3)][lst[i][j]] = 0
check(0)
for i in lst:
    for j in i:
        print(j, end='')
    print()