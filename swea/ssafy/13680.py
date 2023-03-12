ip = int(input())

for i in range(1, ip+1):
    n, target = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    cnt = 0
    ans = list()
    for j in range(n):
        cnt1 = 0
        cnt2 = 0
        for k in range(n):
            if lst[j][k] == 1:
                cnt1 += 1

            else:
                if cnt1:
                    ans.append(cnt1)
                    cnt1 = 0

            if lst[k][j] == 1:
                cnt2 += 1

            else:
                if cnt2:
                    ans.append(cnt2)
                    cnt2 = 0

        if cnt1:
            ans.append(cnt1)

        if cnt2:
            ans.append(cnt2)

    print(f'#{i} {ans.count(target)}')
