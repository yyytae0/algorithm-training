import heapq


def find(a):
    while root[a] != a:
        a = root[a]
    return a


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, [c, a, b])
root = [i for i in range(n+1)]
ans = 0
for _ in range(m):
    i = heapq.heappop(edges)
    a = find(i[1])
    b = find(i[2])
    if a != b:
        if a > b:
            root[a] = b
        else:
            root[b] = a
        ans += i[0]
print(ans)


# 34% 시간초과