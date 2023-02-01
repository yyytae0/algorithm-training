from sys import stdin, stdout


def check(x1, y1, x2, y2):
    global lst
    ans = 0
    for i in range(x1-1, x2):
        if y1 == 1:
            ans += lst[i][y2-1]

        else:
            ans += lst[i][y2-1] - lst[i][y1-2]

    return ans


n, m = map(int, stdin.readline().split())
lst = list()
for i in range(n):
    lst.append(list(map(int, stdin.readline().split())))

for i in range(n):
    for j in range(1, n):
        lst[i][j] = lst[i][j] + lst[i][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    ans = check(x1, y1, x2, y2)
    stdout.write(str(ans)+'\n')
