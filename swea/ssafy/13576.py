ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    big = 0
    for j in range(n):
        cnt = 0
        for k in range(j + 1, n):
            if lst[j] > lst[k]:
                cnt += 1

        if cnt > big:
            big = cnt

    print(f'#{i} {big}')
