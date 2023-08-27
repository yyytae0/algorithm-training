from sys import stdin
import heapq


def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b


def kruskal():
    ans = 0
    while q:
        v = heapq.heappop(q)
        a = find(v[1])
        b = find(v[2])
        if a != b:
            ans += v[0]
            union(v[1], v[2])
    return ans


n = int(stdin.readline())
xlst = []
ylst = []
zlst = []
for i in range(n):
    x, y, z = map(int, stdin.readline().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))
xlst.sort()
ylst.sort()
zlst.sort()
q = []
root = [i for i in range(n)]
for i in range(1, n):
    heapq.heappush(q, (abs(xlst[i][0]-xlst[i-1][0]), xlst[i][1], xlst[i-1][1]))
    heapq.heappush(q, (abs(ylst[i][0] - ylst[i - 1][0]), ylst[i][1], ylst[i - 1][1]))
    heapq.heappush(q, (abs(zlst[i][0] - zlst[i - 1][0]), zlst[i][1], zlst[i - 1][1]))
ans = kruskal()
print(ans)
