from collections import deque


def bfs():
    way = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while queue:
        v = queue.popleft()
        cnt = ans[v[0]][v[1]]
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1]]
            if 0 <= new_v[0] <= m-1 and 0 <= new_v[1] <= n-1:
                if visit[new_v[0]][new_v[1]] == 0 and lst[new_v[0]][new_v[1]] != -1 and lst[new_v[0]][new_v[1]] != 1:
                    visit[new_v[0]][new_v[1]] = 1
                    # if lst[new_v[0]][new_v[1]] == 1:
                    #     queue = []
                    #     break
                    if ans[new_v[0]][new_v[1]] == 0:
                        ans[new_v[0]][new_v[1]] = cnt+1
                        queue.append(new_v)
                    else:
                        if cnt+1 > ans[new_v[0]][new_v[1]]:
                            break
                        else:
                            ans[new_v[0]][new_v[1]] = cnt+1
                            queue.append(new_v)


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(m))
ans = [[0 for _ in range(n)] for _ in range(m)]
queue = deque()
for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            ans[i][j] = 1
            queue.append([i, j])

        if lst[i][j] == -1:
            ans[i][j] = -1

visit = [[0 for _ in range(n)] for _ in range(m)]
bfs()
mx = 0
dummy = 0
for i in range(m):
    if dummy == 1:
        break
    for j in range(n):
        if ans[i][j] == 0:
            mx = 0
            dummy = 1
            break

        else:
            if ans[i][j] > mx:
                mx = ans[i][j]

print(mx-1)
