def dust():
    for i in range(r):
        for j in range(c):
            if lst[i][j] > 0:
                dummy = lst[i][j] // 5
                for dr in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i+dr[0] <= r-1 and 0 <= j+dr[1] <= c-1:
                        if [i+dr[0], j+dr[1]] != [a, 0] and [i+dr[0], j+dr[1]] != [b, 0]:
                            d[i+dr[0]][j+dr[1]] += dummy
                            d[i][j] -= dummy
    for i in range(r):
        for j in range(c):
            lst[i][j] = lst[i][j] + d[i][j]


def clean():
    idx = [a-1, 0]
    while True:
        pass


r, c, t = map(int, input().split())

lst = list(list(map(int, input().split())) for _ in range(r))
d = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    if lst[i][0] == -1:
        a = i
        b = i+1
        break
dust()
for i in lst:
    print(*i)
