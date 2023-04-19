import heapq


def dijkstra(start):
    q = []
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    heapq.heappush(q, [dist[start], start])
    while q:
        v = heapq.heappop(q)
        if dct.get(v[1]):
            for i in dct[v[1]]:
                nv = [v[0] + i[1], i[0]]
                if dist[nv[1]] > nv[0]:
                    dist[nv[1]] = nv[0]
                    heapq.heappush(q, nv)
    cnt = 0
    mx = 0
    for i in dist:
        if i != float('inf'):
            cnt += 1
            if i > mx:
                mx = i
    print(cnt, mx)
    return


ip = int(input())
for case in range(ip):
    n, d, c = map(int, input().split())
    dct = dict()
    for i in range(d):
        a, b, s = map(int, input().split())
        if dct.get(b):
            dct[b].append([a, s])
        else:
            dct[b] = [[a, s]]
    dijkstra(c)
