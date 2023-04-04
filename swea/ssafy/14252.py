import heapq

def dijkstra():
    q = []
    d = [float('inf') for _ in range(n)]
    d[0] = 0
    heapq.heappush(q, [d[0], 0])
    while q:
        v = heapq.heappop(q)
        if v[0] > d[v[1]]:
            continue

        for i in range(n):
            if lst[v[1]][i]:
                nv = [v[0]+lst[v[1]][i], i]
                if nv[0] < d[i]:
                    d[i] = nv[0]
                    heapq.heappush(q, nv)
    return d[n-1]


ip = int(input())

for case in range(1, ip+1):
    n, e = map(int, input().split())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(e):
        a, b, c = map(int, input().split())
        lst[a][b] = c
    ans = dijkstra()
    print(f'#{case} {ans}')
