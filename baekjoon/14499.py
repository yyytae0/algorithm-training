def move(dr):
    if dr == 1:
        if now[1] == m-1:
            return -1
        now[1] += 1
        now[2], now[3], now[4] = 7 - now[3], now[2], now[4]
    elif dr == 2:
        if now[1] == 0:
            return -1
        now[1] -= 1
        now[2], now[3], now[4] = now[3], 7-now[2], now[4]
    elif dr == 3:
        if now[0] == 0:
            return -1
        now[0] -= 1
        now[2], now[3], now[4] = now[4], now[3], 7-now[2]
    else:
        if now[0] == n-1:
            return -1
        now[0] += 1
        now[2], now[3], now[4] = 7-now[4], now[3], now[2]
    if lst[now[0]][now[1]]:
        num[7-now[2]] = lst[now[0]][now[1]]
        lst[now[0]][now[1]] = 0
    else:
        lst[now[0]][now[1]] = num[7-now[2]]
    return num[now[2]]


n, m, x, y, k = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
task = list(map(int, input().split()))
now = [x, y, 1, 3, 5]
num = [0, 0, 0, 0, 0, 0, 0]
for i in task:
    d = move(i)
    if d >= 0:
        print(d)
