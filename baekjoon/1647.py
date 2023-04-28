from sys import stdin
import heapq


def union(a, b):
    na = find(a)
    nb = find(b)
    if na == nb:
        return False
    else:
        if na < nb:
            root[nb] = na
        else:
            root[na] = nb
        return True


def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]


n, m = map(int, stdin.readline().split())
heap = []
root = [i for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    heapq.heappush(heap, [c, a, b])

ans = 0
last = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if union(a, b):
        ans += c
        last = c
ans -= last
print(ans)