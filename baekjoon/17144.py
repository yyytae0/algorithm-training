def dust():
    d = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if lst[i][j] > 0:
                dummy = lst[i][j] // 5
                for dr in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i+dr[0] <= r-1 and 0 <= j+dr[1] <= c-1:
                        if j+dr[1] == 0 and a <= i+dr[0] <= b:
                            continue
                        if [i+dr[0], j+dr[1]] != [a, 0] and [i+dr[0], j+dr[1]] != [b, 0]:
                            d[i+dr[0]][j+dr[1]] += dummy
                            d[i][j] -= dummy
    for i in range(r):
        for j in range(c):
            lst[i][j] = lst[i][j] + d[i][j]


def clean():
    x, y = a-1, 0
    dr = 0
    while True:
        nx, ny = x+way1[dr][0], y+way1[dr][1]
        if not (0 <= nx <= a and 0 <= ny < c):
            dr = (dr+1) % 4
            nx, ny = x+way1[dr][0], y+way1[dr][1]
        if nx == a and ny == 0:
            lst[x][y] = 0
            break
        lst[x][y] = lst[nx][ny]
        x, y = nx, ny
    x, y = b+1, 0
    dr = 0
    while True:
        nx, ny = x+way2[dr][0], y+way2[dr][1]
        if not (b <= nx < r and 0 <= ny < c):
            dr = (dr+1) % 4
            nx, ny = x+way2[dr][0], y+way2[dr][1]
        if nx == b and ny == 0:
            lst[x][y] = 0
            break
        lst[x][y] = lst[nx][ny]
        x, y = nx, ny


r, c, t = map(int, input().split())
way1 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
way2 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
lst = list(list(map(int, input().split())) for _ in range(r))
for i in range(r):
    if lst[i][0] == -1:
        a = i
        b = i+1
        break
for i in range(t):
    dust()
    clean()
ans = 2
for i in lst:
    ans += sum(i)
print(ans)
