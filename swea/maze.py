def bfs(a, b):



ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 3:
                bfs(i, j)