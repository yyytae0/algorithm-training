def check():
    cnt = 0
    for i in range(9):
        for j in range(9):
            if dct1[lst[i][j]] != cnt:
                return 0

            if dct2[lst[j][i]] != cnt:
                return 0

            dct1[lst[i][j]] += 1
            dct2[lst[j][i]] += 1
        cnt += 1

    for i in range(3):
        for j in range(3):
            for n in range(3):
                for m in range(3):
                    if dct1[lst[n + 3*i][m + 3*j]] != cnt:
                        return 0

                    dct1[lst[n + 3*i][m + 3*j]] += 1
            cnt += 1
    return 1


ip = int(input())

for case in range(1, ip+1):
    dct1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    dct2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    lst = list(list(map(int, input().split())) for _ in range(9))
    ans = check()
    print(f'#{case} {ans}')
