from collections import deque


def bfs(a, b):
    global ans
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b, 1, str(lst[a][b])])
    while q:
        v = q.popleft()
        if v[2] > 6:
            break

        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1], v[2] + 1]
            n0 = new_v[0]
            n1 = new_v[1]
            if 0 <= n0 <= 4 and 0 <= n1 <= 4:
                new_v.append(v[3] + str(lst[n0][n1]))
                q.append(new_v)
                if new_v[2] == 6:
                    ans = ans.union([new_v[3]])


ans = set()
lst = list(list(map(int, input().split())) for _ in range(5))
for i in range(5):
    for j in range(5):
        bfs(i, j)
print(len(ans))
