from collections import deque


def bfs():
    q = deque()
    q.append(home)
    while q:
        v = q.popleft()
        for i in lst:
            dist = abs(v[0]-i[0]) + abs(v[1]-i[1])
            if dist <= 1000 and not visit.get(i):
                visit[i] = 1
                q.append(i)
                if i == lst[-1]:
                    return 'happy'
    return 'sad'


ip = int(input())
for case in range(ip):
    n = int(input())
    home = tuple(map(int, input().split()))
    visit = {home: 1}
    lst = list(tuple(map(int, input().split())) for _ in range(n+1))
    # fest = tuple(map(int, input().split()))
    print(bfs())
