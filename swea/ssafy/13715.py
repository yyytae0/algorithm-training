ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(input()) for _ in range(n))
    dummy = 0
    ans = ''
    for i in range(n):
        for k in range(n - m + 1):
            for j in range(m // 2):
                if lst[i][k + j] == lst[i][k + m - j - 1]:
                    dummy = 1
                else:
                    dummy = 0
                    break
            if dummy == 1:
                for j in range(m):
                    ans = ans + lst[i][j+k]
                break
        if dummy == 1:
            break

        for k in range(n - m + 1):
            for j in range(m // 2):
                if lst[k + j][i] == lst[k + m - j - 1][i]:
                    dummy = 1
                else:
                    dummy = 0
                    break
            if dummy == 1:
                for j in range(m):
                    ans = ans + lst[j + k][i]
                break
        if dummy == 1:
            break

    print(f'#{case} {ans}')
