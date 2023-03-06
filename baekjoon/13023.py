def check():
    for a in range(n):
        visit[a] = 1
        for b in lst[a]:
            if not visit[b]:
                visit[b] = 1
                for c in lst[b]:
                    if not visit[c]:
                        visit[c] = 1
                        for d in lst[c]:
                            if not visit[d]:
                                visit[d] = 1
                                for e in lst[d]:
                                    if not visit[e]:
                                        return 1
                                visit[d] = 0
                        visit[c] = 0
                visit[b] = 0
        visit[a] = 0
    return 0


n, m = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
visit = [0 for _ in range(n)]
print(check())
