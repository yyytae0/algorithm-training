def check(cnt):
    if cnt == n:
        print(*ans)
        return

    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            ans.append(i)
            check(cnt + 1)
            ans.pop()
            visit[i] = 0


n = int(input())
visit = [0 for _ in range(n+1)]
ans = []
check(0)