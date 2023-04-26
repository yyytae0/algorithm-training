import heapq


def dijkstra():
    q = []
    d = [[float('inf') for _ in range(k+1)] for _ in range(n+1)]
    d[1] = [0 for _ in range(k+1)]
    heapq.heappush(q, [0, 1, 0])
    while q:
        dist, now, cover = heapq.heappop(q)
        if dist > d[now][cover]:
            continue
        for i, j in lst[now]:
            dummy = j
            if d[i][cover] > dummy+dist:
                d[i][cover] = dummy+dist
                heapq.heappush(q, [d[i][cover], i, cover])
            if cover < k:
                if d[i][cover+1] > dist:
                    d[i][cover+1] = dist
                    heapq.heappush(q, [d[i][cover+1], i, cover+1])
    print(min(d[n]))


n, m, k = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[b].append([a, c])
    lst[a].append([b, c])
dijkstra()
