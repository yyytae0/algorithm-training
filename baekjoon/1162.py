import heapq


def dijkstra():
    q = []
    d = [[float('inf') for _ in range(n+1)] for _ in range(k+1)]
    d[1][0] = 0
    heapq.heappush(q, [d[1][0], 1, 0])
    while q:
        v = heapq.heappop(q)
        if v[0] > d[v[2]][v[1]]:
            continue
        for i in lst[v[1]]:
            dummy = lst[v[1]][i]
            if d[v[2]][i] > dummy+v[0]:
                d[v[2]][i] = dummy+v[0]
                heapq.heappush(q, [d[v[2]][i], i, v[2]])
            if v[2] < k:
                if d[v[2]+1][i] > v[0]:
                    d[v[2]+1][i] = v[0]
                    heapq.heappush(q, [d[v[2]+1][i], i, v[2]+1])
    mn = d[-1][-1]
    for i in d:
        mn = min(mn, i[-1])
    print(mn)


n, m, k = map(int, input().split())
lst = [{} for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[b][a] = c
    lst[a][b] = c
dijkstra()