import heapq


def find(a):
    while root[a] != a:
        a = root[a]
    return a


ip = int(input())

for case in range(1, ip+1):
    v, e = map(int, input().split())
    edges = []
    for i in range(e):
        a, b, c = map(int, input().split())
        heapq.heappush(edges, [c, a, b])
    root = [i for i in range(v+1)]
    ans = 0
    for _ in range(e):
        i = heapq.heappop(edges)
        a = find(i[1])
        b = find(i[2])
        if a != b:
            if a > b:
                root[a] = b
            else:
                root[b] = a
            ans += i[0]
    print(f'#{case} {ans}')
