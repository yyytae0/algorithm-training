ip = int(input())
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    ans = [[0 for _ in range(n)] for _ in range(n)]
    total = 0
    for x in range(0, n):
        for y in range(0, n):
            for j in range(4):
                if 0 <= x+dx[j] < n and 0 <= y+dy[j] < n:
                    dummy = lst[x][y] - lst[x+dx[j]][y+dy[j]]
                    total = total + dummy if dummy > 0 else total - dummy

            ans[x][y] = total

    print(f'#{i} {total}')
