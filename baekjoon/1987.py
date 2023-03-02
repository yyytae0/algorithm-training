def dfs(a, b, cnt):
    global mx
    if cnt > mx:
        mx = cnt
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in way:
        if 0 <= a+i[0] < r and 0 <= b+i[1] < c and visit[lst[a+i[0]][b+i[1]]]:
            visit[lst[a+i[0]][b+i[1]]] = 0
            dfs(a+i[0], b+i[1], cnt+1)
            visit[lst[a+i[0]][b+i[1]]] = 1


r, c = map(int, input().split())
lst = list(list(input()) for _ in range(r))
for i in range(r):
    for j in range(c):
        lst[i][j] = ord(lst[i][j]) - 65
mx = 0
visit = [1 for _ in range(26)]
visit[lst[0][0]] = 0
dfs(0, 0, 1)
print(mx)
