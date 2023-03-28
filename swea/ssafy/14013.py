def check(a):
    global ans, sm
    if sm > ans:
        return
    if a == n:
        if sm < ans:
            ans = sm
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            sm += lst[a][i]
            check(a+1)
            visit[i] = 0
            sm -= lst[a][i]


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    visit = [0 for _ in range(n)]
    ans, sm = 10**5, 0
    check(0)
    print(f'#{case} {ans}')
