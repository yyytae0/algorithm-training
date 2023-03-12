ip = int(input())
for i in range(1, ip+1):
    lst = list()
    n = int(input())
    for j in range(n):
        lst.append(list(map(int, input().split())))

    ans = [0 for _ in range(1001)]

    for j in lst:
        if j[0] == 1:
            for k in range(j[1], j[2]+1):
                ans[k] += 1

        elif j[0] == 2:
            for k in range(j[1], j[2]+1, 2):
                ans[k] += 1

            if (j[1]+j[2])%2 == 1:
                ans[j[2]] += 1

        elif j[0] == 3:
            for k in range(j[1], j[2]+1):
                if j[1]%2 == 0:
                    if k % 4 == 0:
                        ans[k] += 1

                    elif k == j[1]:
                        ans[k] += 1

                    elif k == j[2]:
                        ans[k] += 1

                else:
                    if k % 3 == 0 and k % 10 != 0:
                        ans[k] += 1

                    elif k == j[1]:
                        ans[k] += 1

                    elif k == j[2]:
                        ans[k] += 1

    print(f'#{i}', max(ans))
