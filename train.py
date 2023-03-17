n, m, k = map(int, input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])