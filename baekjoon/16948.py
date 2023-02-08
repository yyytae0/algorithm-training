from collections import deque


def bfs():
    way = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
    q = deque()
    q.append([x1, y1, 0])
    visit[x1][y1] = 1
    while q:
        v = q.popleft()
        for i in way:
            new_v = [v[0]+i[0], v[1]+i[1], v[2]+1]
            n0 = new_v[0]
            n1 = new_v[1]
            if 0 <= n0 <= n-1 and 0 <= n1 <= n-1 and not visit[n0][n1]:
                q.append(new_v)
                visit[n0][n1] = 1
                if [n0, n1] == [x2, y2]:
                    return v[2]+1
    return -1


n = int(input())
x1, y1, x2, y2 = map(int, input().split())
if [x1, y1] == [x2, y2]:
    print(0)

else:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    print(bfs())
