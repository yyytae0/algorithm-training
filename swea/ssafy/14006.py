ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    lst.sort(key=lambda x: (x[1], x[0]))
    now = lst[0]
    ans = 1
    for i in range(1, n):
        if lst[i][0] >= now[1]:
            ans += 1
            now = lst[i]
    print(f'#{case} {ans}')
