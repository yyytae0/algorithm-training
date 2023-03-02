import heapq
from sys import stdin


def dijkstra(a, b):
    q = []
    d = [float('inf') for _ in range(n+1)]
    d[a] = 0
    heapq.heappush(q, [a, d[a]])
    while q:
        v = heapq.heappop(q)

        if v[1] > d[v[0]]:
            continue

        for i in lst[v[0]]:
            nv = [i[0], v[1]+i[1]]
            if d[i[0]] > nv[1]:
                heapq.heappush(q, nv)
                d[i[0]] = nv[1]
    return d[b]


n = int(stdin.readline())
m = int(stdin.readline())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    lst[a].append([b, c])
a, b = map(int, stdin.readline().split())
print(dijkstra(a, b))
