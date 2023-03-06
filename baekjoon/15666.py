def check(a, cnt):
    if cnt == m:
        ans.append(d[:])
        return

    for i in range(a, n):
        d.append(lst[i])
        check(i, cnt+1)
        d.pop()


n, m = map(int, input().split())
lst = list(set(map(int, input().split())))
lst.sort()
n = len(lst)
d = []
ans = []
check(0, 0)
for i in ans:
    print(*i)
