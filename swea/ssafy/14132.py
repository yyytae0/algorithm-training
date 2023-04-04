def move():
    dct = dict()
    for i in range(1, k+1):
        if cell[i]:
            a, b, c, d = cell[i][0], cell[i][1], cell[i][2], cell[i][3]
            na, nb = a + way[d][0], b + way[d][1]
            cell[i] = [na, nb, c, d]
            if dct.get((na, nb)):
                dct[(na, nb)].append(i)
            else:
                dct[(na, nb)] = [i]
    for i in dct:
        mx = 0
        idx = 0
        sm = 0
        for j in dct[i]:
            sm += cell[j][2]
            if cell[j][2] > mx:
                mx = cell[j][2]
                idx = j
        cell[idx][2] = sm
        for j in dct[i]:
            if j != idx:
                cell[j] = []

        if cell[idx][0] == 0 or cell[idx][0] == n-1 or cell[idx][1] == 0 or cell[idx][1] == n-1:
            cell[idx][2] = cell[idx][2]//2
            cell[idx][3] = change[cell[idx][3]]


ip = int(input())
way = [[0, 1], [-1, 0], [1, 0], [0, -1]]
change = [3, 2, 1, 0]
for case in range(1, ip+1):
    n, m, k = map(int, input().split())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    cell = [[] for _ in range(k+1)]
    for i in range(1, k+1):
        a, b, c, d = map(int, input().split())
        cell[i] = [a, b, c, d%4]
        lst[a][b] = i

    for i in range(m):
        move()
    ans = 0
    for i in cell:
        if i:
            ans += i[2]
    print(f'#{case} {ans}')
