ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    mx = lst[-1]
    cnt = 0
    cost = 0
    for i in range(n-2, -1, -1):
        if lst[i] <= mx:
            cnt += 1
            cost -= lst[i]

        else:
            cost += cnt*mx
            cnt = 0
            mx = lst[i]

    cost += cnt*mx
    print(f'#{case} {cost}')
