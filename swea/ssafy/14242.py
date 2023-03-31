def check(a, now):
    global ans
    if a == n:
        if now > ans:
            ans = now
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            new = now*lst[a][i]/100
            if new > ans:
                check(a+1, now*lst[a][i]/100)
            visit[i] = 0


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    ans = 0
    lst = list(list(map(int, input().split())) for _ in range(n))
    visit = [0 for _ in range(n)]
    check(0, 1)
    ans = round(ans*100, 6)
    print(f'#{case} {ans:.6f}')
