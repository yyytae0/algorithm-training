def game():
    global now, ans
    for i in range(n):
        if lst[i][now]:
            shk[lst[i][now]][0] = 0
            ans += shk[lst[i][now]][5]
            lst[i][now] = 0
            break
    for i in range(1, shark+1):
        if shk[i][0]:
            shk[i][0] += 1
            x, y = shk[i][1], shk[i][2]
            if lst[x][y] == i:
                lst[x][y] = 0
            move(i)
            nx, ny = shk[i][1], shk[i][2]
            if lst[nx][ny]:
                if shk[lst[nx][ny]][0] == shk[i][0]:
                    if not eat(lst[nx][ny], i):
                        lst[nx][ny] = i
                else:
                    lst[nx][ny] = i
            else:
                lst[nx][ny] = i


def move(a):
    x, y = shk[a][1], shk[a][2]
    s = shk[a][3]
    dr = way[shk[a][4]]
    for i in range(s):
        x += dr[0]
        y += dr[1]
        if x<0 or x>=n or y<0 or y>=m:
            shk[a][4] = change[shk[a][4]]
            dr = way[shk[a][4]]
            x += dr[0]*2
            y += dr[1]*2
    shk[a][1] = x
    shk[a][2] = y


def eat(a, b):
    if shk[a][5] > shk[b][5]:
        shk[b][0] = 0
        return True
    else:
        shk[a][0] = 0
        return False


way = [[0, -1], [-1, 0], [1, 0], [0, 1]]
change = [3, 2, 1, 0]
n, m, shark = map(int, input().split())
lst = [[0 for _ in range(m)] for _ in range(n)]
shk = [[0 for _ in range(6)] for _ in range(shark+1)]
now = 0
for i in range(1, shark+1):
    x, y, a, b, c = map(int, input().split())
    if b == 1 or b == 2:
        a = a % (2*n-2)
    else:
        a = a % (2*m-2)
    lst[x-1][y-1] = i
    shk[i] = [1, x-1, y-1, a, b % 4, c]
ans = 0
for i in range(m):
    # for j in lst:
    #     print(*j)
    # print('-----------')
    game()
    now += 1
print(ans)
