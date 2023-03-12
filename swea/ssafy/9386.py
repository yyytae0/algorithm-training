ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = list(input())
    cnt = 0
    mx = 0
    for j in lst:
        if j == '0':
            cnt = 0

        else:
            cnt += 1
            if cnt > mx:
                mx = cnt

    print(f'#{i} {mx}')
