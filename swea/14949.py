ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    mx = 0
    for i in range(n):
        cnt1 = 0
        for j in range(m):
            if lst[i][j] == 1:
                cnt1 += 1
            elif lst[i][j] == 0:
                if cnt1 > mx:
                    mx = cnt1
                cnt1 = 0
        if cnt1 > mx:
            mx = cnt1

    for i in range(m):
        cnt1 = 0
        for j in range(n):
            if lst[j][i] == 1:
                cnt1 += 1
            elif lst[j][i] == 0:
                if cnt1 > mx:
                    mx = cnt1
                cnt1 = 0
        if cnt1 > mx:
            mx = cnt1
    print(f'#{case} {mx}')
