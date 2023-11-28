

def dfs(nx, ny, cnt):
    if visit[nx][ny] == -1 or nx >= a or nx < 0 or ny >= b or ny < 0:
        return -1
    if visit[nx][ny] == cnt:
        return

    if lst[nx][ny] == 'U':
        tx, ty = nx-1, ny
    elif lst[nx][ny] == 'L':
        tx, ty = nx, ny-1
    elif lst[nx][ny] == 'D':
        tx, ty = nx+1, ny
    else:
        tx, ty = nx, ny+1

    visit[nx][ny] = dfs(tx, ty, cnt)



a, b = map(int, input().split())

lst = []
cost = []
visit = [[0 for _ in range(b)] for _ in range(a)]

for i in range(a):
    lst.append(list(input()))

for i in range(a):
    cost.append(list(map(int, input().split())))

for i in range(a):
    for j in range(b):
