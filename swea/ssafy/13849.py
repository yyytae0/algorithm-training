def check(c, sm):
    global ans
    if sm > ans:
        return

    if c == n:
        if ans > sm:
            ans = sm
        return

    for i in range(n):
        if d[i]:
            d[i] = False
            check(c+1, sm+lst[c][i])
            d[i] = True


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    d = [True for _ in range(n)]
    ans = 100
    check(0, 0)
    print(f'#{case} {ans}')
