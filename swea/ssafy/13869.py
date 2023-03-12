ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = [0] * n
    for j in lst:
        cnt = 0
        for k in lst:
            if j > k:
                cnt += 1

        while ans[cnt] > 0:
            cnt += 1

        ans[cnt] = j

    print(f'#{i}', *ans)
