for case in range(1, 11):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    cnt = 0
    for j in range(n):
        d = 0
        for i in range(n):
            if lst[i][j] == 1:
                d += 1
            elif lst[i][j] == 2:
                if d:
                    d = 0
                    cnt += 1
    print(f'#{case} {cnt}')