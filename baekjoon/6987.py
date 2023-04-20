def dfs(n):
    if n == 36:
        return 1
    y = n//6
    x = n % 6
    if x == y or score[x][y] >= 0:
        return dfs(n+1)

    for i in [0, 1, 2]:
        if lst[y*3+i] and lst[x*3+2-i]:
            lst[y*3+i] -= 1
            lst[x*3+2-i] -= 1
            score[y][x] = i
            score[x][y] = 2-i
            if dfs(n+1):
                return 1
            score[y][x] = -1
            score[x][y] = -1
            lst[y*3+i] += 1
            lst[x*3+2-i] += 1
    return 0


def check():
    for i in range(6):
        sm = 0
        for j in range(3):
            sm += lst[3*i+j]
        if sm != 5:
            return 0
    return 1


for case in range(4):
    lst = list(map(int, input().split()))
    score = [[-1 for _ in range(6)] for _ in range(6)]
    if check():
        print(dfs(0), end=' ')
    else:
        print(0, end=' ')
