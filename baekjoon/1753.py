import heapq


def dijkstra(start):
    q = []
    d = [float('INF') for _ in range(n+1)]
    d[start] = 0
    heapq.heappush(q, [d[start], start])
    while q:
        v = heapq.heappop(q)

        if d[v[1]] < v[0]:
            continue

        for i in dct[v[1]]:
            nv = [v[0] + i[1], i[0]]
            if nv[0] < d[nv[1]]:
                d[nv[1]] = nv[0]
                heapq.heappush(q, nv)
    return d


n, m = map(int, input().split())
k = int(input())
dct = dict()
for i in range(1, n+1):
    dct[i] = []
for i in range(m):
    a, b, c = map(int, input().split())
    dct[a].append([b, c])
ans = dijkstra(k)[1:]
for i in ans:
    if i == float('inf'):
        print('INF')
    else:
        print(i)
