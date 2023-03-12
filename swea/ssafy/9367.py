ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    dummy = 0
    cnt = 0
    mx = 0
    for j in lst:
        if j > dummy:
            cnt += 1
            dummy = j
            if cnt > mx:
                mx = cnt

        else:
            dummy = j
            cnt = 1

    print(f'#{i} {mx}')
