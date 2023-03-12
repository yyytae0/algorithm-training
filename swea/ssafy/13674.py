ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    ans = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for j in range(n):
        lst = list(map(int, input().split()))
        if lst[-1] == 1:
            for x in range(lst[0], lst[2]+1):
                for y in range(lst[1], lst[3]+1):
                    if ans[x][y] == 3:
                        continue

                    elif ans[x][y] == 2:
                        ans[x][y] = 3
                        cnt += 1

                    else:
                        ans[x][y] = 1

        elif lst[-1] == 2:
            for x in range(lst[0], lst[2]+1):
                for y in range(lst[1], lst[3]+1):
                    if ans[x][y] == 3:
                        continue

                    elif ans[x][y] == 1:
                        ans[x][y] = 3
                        cnt += 1

                    else:
                        ans[x][y] = 2

    print(f'#{i} {cnt}')
