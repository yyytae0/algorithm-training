import heapq


def dijkstra(start):
    q = []
    d = [float('inf') for _ in range(n+1)]
    d[start] = 0
    heapq.heappush(q, [start, d[start]])
    while q:
        v = heapq.heappop(q)

        if d[v[0]] < v[1]:
            continue

        for i in dct[v[0]]:
            nv = [i[0], v[1]+i[1]]
            if nv[1] < d[nv[0]]:
                d[nv[0]] = nv[1]
                heapq.heappush(q, nv)
    for i in range(n+1):
        if d[i] == float('inf'):
            d[i] = 0
    return d


n = int(input())
m = int(input())
dct = dict()
for i in range(1, n+1):
    dct[i] = []
for _ in range(m):
    a, b, c = map(int, input().split())
    dct[a].append([b, c])
for i in range(1, n+1):
    ans = dijkstra(i)
    print(*ans[1:])
