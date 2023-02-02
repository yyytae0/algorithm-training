from sys import stdin, stdout


def check(x1, y1, x2, y2):
    global lst
    if x1 == 0 and y1 == 0:
        return lst[x2][y2]

    elif x1 == 0:
        return lst[x2][y2] - lst[x2][y1-1]

    elif y1 == 0:
        return lst[x2][y2] - lst[x1-1][y2]

    else:
        return lst[x2][y2] - lst[x1-1][y2] - lst[x2][y1-1] + lst[x1-1][y1-1]


n, m = map(int, stdin.readline().split())
lst = list()
for i in range(n):
    lst.append(list(map(int, stdin.readline().split())))

for i in range(n):
    if i != 0:
        lst[i][0] = lst[i][0] + lst[i-1][0]
    for j in range(1, n):
        if i == 0:
            lst[i][j] = lst[i][j] + lst[i][j-1]

        else:
            lst[i][j] = lst[i][j] + lst[i-1][j] + lst[i][j-1] -lst[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    s = check(x1-1, y1-1, x2-1, y2-1)
    stdout.write(str(s)+'\n')
