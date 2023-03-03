def check(a, cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(a+1, n):
        ans.append(lst[i])
        check(i, cnt+1)
        ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(n):
    ans = [lst[i]]
    check(i, 1)
