import heapq


def dijkstra(start):
    q = []
    dist = [float('inf') for _ in range(n+1)]
    dist[start] = 0
    heapq.heappush(q, [dist[start], start])
    while q:
        v = heapq.heappop(q)
        for i in range(1, n+1):
            if lst[v[1]][i] and dist[i] > v[0]+1:
                dist[i] = v[0] + 1
                heapq.heappush(q, [v[0]+1, i])
    cnt = 0
    for i in range(1, n+1):
        if dist[i] > cnt:
            cnt = dist[i]
    return cnt


def check():
    for i in range(1, n+1):
        if ans[i]:
            return i, ans[i]


n = int(input())
lst = [[0 for _ in range(n+1)] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    lst[a][b] = 1
    lst[b][a] = 1

ans = [[] for _ in range(n+1)]
for i in range(1, n+1):
    d = dijkstra(i)
    ans[d].append(i)

score, chk = check()
print(score, len(chk))
print(*chk)
