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
            if d[i[0]] > nv[0]:
                heapq.heappush(q, nv)
                d[i[0]] = nv[0]
    return d[x]


n, m, x = map(int, input().split())
d = [float('inf') for _ in range(n+1)]
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
dijkstra(x)
ans = d[1:]
for i in range(1, n+1):
    d = [float('inf') for _ in range(n + 1)]
    ans[i-1] += dijkstra(i)
print(max(ans))
