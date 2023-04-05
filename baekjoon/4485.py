from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    visit[0][0] = lst[0][0]
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < n:
                d = visit[v[0]][v[1]] + lst[nv[0]][nv[1]]
                if d < visit[nv[0]][nv[1]]:
                    visit[nv[0]][nv[1]] = d
                    q.append(nv)


n = int(input())
way = [[1, 0], [0, 1], [-1, 0], [0, -1]]
case = 1
while n:
    lst = list(list(map(int, input().split())) for _ in range(n))
    visit = [[float('inf') for _ in range(n)] for _ in range(n)]
    bfs()
    print(f'Problem {case}: {visit[-1][-1]}')
    case += 1
    n = int(input())