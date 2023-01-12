


def make_maze(scale):
    maze = list()
    for i in range(scale):
        a = input()
        dum = list()
        for j in range(scale):
            dum.append(a[k])
        maze.append(dum)
    return maze

def escape(maze, scale):
    result = 1
    while True:
        if maze[1][2] == '1':
            if maze[2][1] == '1':
                result = 0
                break

        for i in range(1, scale):
            for j in range(1, scale):
                if maze[j][k] == '0':
                    cnt = 0
                    if maze[j - 1][k] == '1':
                        cnt += 1

                    if maze[j + 1][k] == '1':
                        cnt += 1

                    if maze[j][k + 1] == '1':
                        cnt += 1

                    if maze[j][k - 1] == '1':
                        cnt += 1

                    if cnt >= 3:
                        maze[j][k] = '1'

    return result




"""
ans = list()

for i in range(10):
    ip = int(input())
    maze = list()
    for j in range(100):
        a = input()
        lst = list()
        for k in range(100):
            lst.append(a[k])
        maze.append(lst)

    for n in range(5000):
        for j in range(1, 100):
            for k in range(1, 100):
                if maze[j][k] == '0':
                    cnt = 0
                    if maze[j - 1][k] == '1':
                        cnt += 1

                    if maze[j + 1][k] == '1':
                        cnt += 1

                    if maze[j][k + 1] == '1':
                        cnt += 1

                    if maze[j][k - 1] == '1':
                        cnt += 1

                    if cnt >= 3:
                        maze[j][k] = '1'

    answer = 1
    if maze[1][2] == '1':
        if maze[2][1] == '1':
            answer = 0

    ans.append([i, answer])

for i in range(10):
    print("#%d %d" % (ans[i][0] + 1, ans[i][1]))
"""
