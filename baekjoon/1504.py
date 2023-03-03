import heapq


def dijkstra(s):
    q = []
    d[s] = 0
    heapq.heappush(q, [d[s], s])
    while q:
        v = heapq.heappop(q)
        if d[v[1]] < v[0]:
            continue

        for i in lst[v[1]]:
            nv = [v[0] + i[1], i[0]]
            if d[nv[1]] > nv[0]:
                heapq.heappush(q, nv)
                d[i[0]] = nv[0]
    return d


n, e = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
a, b = map(int, input().split())
d = [float('inf') for _ in range(n+1)]
dijkstra(1)
ans1 = d[a]
ans2 = d[b]
d = [float('inf') for _ in range(n+1)]
dijkstra(a)
ans1 += d[b]
ans2 += d[n]
d = [float('inf') for _ in range(n+1)]
dijkstra(b)
ans1 += d[n]
ans2 += d[a]
if ans1 == float('inf') and ans2 == float('inf'):
    print(-1)
else:
    print(min(ans1, ans2))
