def solv(a, cnt):
    if cnt == m:
        print(*ans)
        return

    for i in range(n):
        if not visit[lst[i]]:
            ans.append(lst[i])
            visit[lst[i]] = 1
            solv(i, cnt + 1)
            visit[lst[i]] = 0
            ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
visit = [0 for _ in range(10001)]
lst.sort()
ans = []
solv(-1, 0)
