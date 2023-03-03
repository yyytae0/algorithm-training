def check(cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(lst[i])
        check(cnt+1)
        ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
check(0)