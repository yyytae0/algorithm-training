import heapq


def calc(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)**(1/2)


def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]


n = int(input())
dist = [[float("inf") for _ in range(n)] for _ in range(n)]
lst = [list(map(float, input().split())) for _ in range(n)]
edges = []
root = [i for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        d = calc(lst[i][0], lst[i][1], lst[j][0], lst[j][1])
        heapq.heappush(edges, [d, i, j])

while edges:
    e = heapq.heappop(edges)
    a = find(e[1])
    b = find(e[2])
    if a != b:
        root[b] = a
        ans += e[0]
print(ans)
