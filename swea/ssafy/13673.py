ip = int(input())

for i in range(1, ip+1):
    lst = list(list(map(int, input().split())) for _ in range(100))
    total3 = 0
    total4 = 0
    mx = 0
    for j in range(100):
        total1 = 0
        total2 = 0
        for k in range(100):
            total1 += lst[j][k]
            total2 += lst[k][j]
            if j == k:
                total3 += lst[j][k]

            if j == 99-k:
                total4 += lst[j][k]

        mx = max(mx, total1, total2)

    mx = max(mx, total3, total4)
    print(f'#{i} {mx}')
