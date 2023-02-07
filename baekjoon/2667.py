def bfs(a, b):
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = [[a, b]]
    visit[a][b] = 1
    cnt = 1
    while queue:
        v = queue[0]
        del queue[0]
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1:
                if visit[new_v[0]][new_v[1]] == 0 and lst[new_v[0]][new_v[1]] == 1:
                    queue.append([new_v[0], new_v[1]])
                    visit[new_v[0]][new_v[1]] = 1
                    cnt += 1

    return cnt


n = int(input())
lst = list(list(map(int, input())) for _ in range(n))
visit = [[0 for _ in range(n)] for _ in range(n)]
ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1 and visit[i][j] == 0:
            a = bfs(i, j)
            ans.append(a)
            cnt += 1
ans.sort()
print(cnt)
for i in ans:
    print(i)
