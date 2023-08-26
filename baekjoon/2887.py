from sys import stdin
import heapq


# def prim(start):
#     ans = 0
#     q = graph[start]
#     visit[start] = 1
#     while q:
#         d, e = heapq.heappop(q)
#         if not visit[e]:
#             visit[e] = 1
#             ans += d
#             for nd, ne in graph[e]:
#                 if not visit[ne]:
#                     heapq.heappush(q, [nd, ne])
#     return ans


def prim2(start):
    ans = 0
    visit[start] = 1
    while q:
        d, e = heapq.heappop(q)
        if not visit[e]:
            visit[e] = 1
            ans += d
            for i in range(n):
                d = dist[e][i]
                if not visit[i] and d < waiting[i]:
                    heapq.heappush(q, [d, i])
                    waiting[i] = d
    return ans


n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(n)]
dist = [[float("inf") for _ in range(n)] for _ in range(n)]
waiting = [float("inf") for _ in range(n)]
waiting[0] = 0
visit = [0 for _ in range(n)]
q = []
for i in range(n):
    for j in range(i+1, n):
        d = min(abs(lst[i][0]-lst[j][0]), abs(lst[i][1]-lst[j][1]), abs(lst[i][2]-lst[j][2]))
        dist[i][j], dist[j][i] = d, d
        if i == 0:
            heapq.heappush(q, [d, j])
            waiting[j] = d
ans = prim2(0)
print(ans)
