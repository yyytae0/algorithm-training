from sys import stdin
import heapq


def dijkstra():
    q = list()
    d[s][0] = 0
    heapq.heappush(q, [d[s][0], s])
    while q:
        v = heapq.heappop(q)
        if d[v[1]][0] < v[0]:
            continue
        for i in dct[v[1]]:
            nv = [v[0]+i[1], i[0]]
            if d[nv[1]][0] >= nv[0]:
                heapq.heappush(q, nv)
                d[nv[1]][0] = nv[0]
                if (i[0] == g and v[1] == h) or (i[0] == h and v[1] == g) or d[v[1]][1]:
                    d[nv[1]][1] = 1


ip = int(stdin.readline())

for case in range(ip):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())
    dct = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        dct[i] = []
    for i in range(m):
        a, b, d = map(int, stdin.readline().split())
        dct[a].append([b, d])
        dct[b].append([a, d])
    d = [[float('inf'), 0] for _ in range(n+1)]
    dijkstra()
    ans = []
    for i in range(t):
        a = int(stdin.readline())
        if d[a][1] == 1:
            ans.append(a)
    ans.sort()
    print(*ans)



# from sys import stdin
# import heapq
#
#
# def dijkstra():
#     q = list()
#     d[s] = 0
#     heapq.heappush(q, [d[s], s])
#     while q:
#         v = heapq.heappop(q)
#         if d[v[1]] < v[0]:
#             continue
#         for i in dct[v[1]]:
#             nv = [v[0] + i[1], i[0]]
#             if d[nv[1]] > nv[0]:
#                 heapq.heappush(q, nv)
#                 d[nv[1]] = nv[0]
#
#
# ip = int(stdin.readline())
#
# for case in range(ip):
#     n, m, t = map(int, stdin.readline().split())
#     s, g, h = map(int, stdin.readline().split())
#     dct = [[] for _ in range(n+1)]
#     for i in range(m):
#         a, b, dd = map(int, stdin.readline().split())
#         if (a == g and b == h) or (a == h and b == g):
#             dct[a].append([b, 2*dd - 1])
#             dct[b].append([a, 2*dd - 1])
#         else:
#             dct[a].append([b, 2 * dd])
#             dct[b].append([a, 2 * dd])
#     d = [float('inf') for _ in range(n + 1)]
#     dijkstra()
#     ans = []
#     for i in range(t):
#         a = int(stdin.readline())
#         if d[a]%2 == 1:
#             ans.append(a)
#     ans.sort()
#     print(*ans)

