def check(a, cnt):
    global d, ans
    if cnt == m:
        ans.append(' '.join(d))
        return

    for i in range(a+1, n):
        d.append(str(lst[i]))
        check(i, cnt+1)
        d.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
d, ans = [], []
check(-1, 0)
ans = list(set(ans))
ans = list(list(map(int, i.split())) for i in ans)
ans.sort()
for i in ans:
    print(*i)
