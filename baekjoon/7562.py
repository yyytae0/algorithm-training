from collections import deque


def bfs(a, b):
    way = [[2, 1], [1, 2], [2, -1], [1, -2], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]
    q = deque()
    q.append([a, b, 0])
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0] + i[0], v[1] + i[1], v[2] + 1]
            if 0 <= new_v[0] <= n-1 and 0 <= new_v[1] <= n-1 and not visit[new_v[0]][new_v[1]]:
                if [new_v[0], new_v[1]] == target:
                    return new_v[2]
                q.append(new_v)
                visit[new_v[0]][new_v[1]] = 1


ip = int(input())
for case in range(ip):
    n = int(input())
    x, y = map(int, input().split())
    target = list(map(int, input().split()))
    if [x, y] == target:
        print(0)

    else:
        visit = [[0 for _ in range(n)] for _ in range(n)]
        ans = bfs(x, y)
        print(ans)
