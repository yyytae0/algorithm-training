import heapq
from sys import stdin


def dijkstra():
    q = list()
    d[s][0] = 0
    d[s][1] = [s]
    heapq.heappush(q, [d[s][0], s])
    while q:
        v = heapq.heappop(q)
        if d[v[1]][0] < v[0]:
            continue

        for i in dct[v[1]]:
            nv = [v[0]+i[1], i[0]]
            if d[nv[1]][0] > nv[0]:
                heapq.heappush(q, nv)
                d[nv[1]][0] = nv[0]
                d[nv[1]][1] = d[v[1]][1] + [i[0]]


n = int(stdin.readline())
m = int(stdin.readline())
d = [[float('inf'), []] for _ in range(n+1)]
dct = dict()
for i in range(1, n+1):
    dct[i] = []
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    dct[a].append([b, c])

s, g = map(int, stdin.readline().split())
dijkstra()
print(d[g][0])
print(len(d[g][1]))
print(*d[g][1])
