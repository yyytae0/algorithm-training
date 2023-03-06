def check(cnt):
    if cnt == m:
        ans.append(' '.join(d))
        return

    for i in range(n):
        if not visit[i]:
            d.append(str(lst[i]))
            visit[i] = 1
            check(cnt + 1)
            visit[i] = 0
            d.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
d = []
visit = [0 for _ in range(n)]
check(0)
ans = set(ans)
ans = list(list(map(int, i.split())) for i in ans)
ans.sort()
for i in ans:
    print(*i)
