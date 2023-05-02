from collections import deque


def bfs():
    q = deque()
    q.append([1, 0])
    while q:
        v = q.popleft()
        for i in range(1, 7):
            nv = [v[0]+i, v[1]+1]
            nv[0] = ladder[nv[0]]
            if 1 <= nv[0] <= 100 and nv[1] <= dp[nv[0]]:
                dp[nv[0]] = nv[1]
                q.append(nv)
                if nv[0] == 100:
                    return nv[1]


n, m = map(int, input().split())
ladder = [i for i in range(101)]
dp = [float('inf') for _ in range(101)]
for i in range(n+m):
    a, b = map(int, input().split())
    ladder[a] = b
print(bfs())
