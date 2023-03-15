import heapq


def dijkstra():
    q = []
    dp[0] = 0
    heapq.heappush(q, [dp[0], 0])
    while q:
        v = heapq.heappop(q)
        if dp[v[1]] < v[0]:
            continue
        for i in dct[v[1]]:
            nv = [v[0] + i[1], i[0]]
            if nv[0] >= dp[nv[1]]:
                continue
            heapq.heappush(q, nv)
            dp[nv[1]] = nv[0]


n, d = map(int, input().split())
dct = dict()
dp = [float('inf') for _ in range(d+1)]
for i in range(d):
    dct[i] = [[i+1, 1]]
dct[d] = []
for i in range(n):
    a, b, c = map(int, input().split())
    if b > d or a >= d:
        continue
    dct[a].append([b, c])
dijkstra()
print(dp[d])
