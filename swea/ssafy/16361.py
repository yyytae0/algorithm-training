for case in range(1, 11):
    n = int(input())
    lst = list(input() for _ in range(8))
    cnt = 0
    if n == 1:
        print(f'#{case} 64')
    else:
        for i in range(8):
            for j in range(8-n+1):
                for k in range(n//2):
                    if lst[i][j+k] != lst[i][j+n-k-1]:
                        break
                else:
                    cnt += 1

            for j in range(8 - n + 1):
                for k in range(n // 2):
                    if lst[j+k][i] != lst[j + n - k - 1][i]:
                        break
                else:
                    cnt += 1
        print(f'#{case} {cnt}')
