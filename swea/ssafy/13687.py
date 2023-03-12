ip = int(input())
for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    lst.sort()
    remain = lst[:]
    cnt = 0
    while remain:
        cnt += 1
        d_lst = list()
        dummy = 0
        for i in remain:
            if (i[0]//2 + i[0]%2) > dummy and (i[1]//2 + i[1]%2) > dummy:
                dummy = max((i[0]//2 + i[0]%2), (i[1]//2 + i[1]%2))
            else:
                d_lst.append(i)
        remain = d_lst[:]
    print(f'#{case} {cnt}')
