ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(str, input().split())) for _ in range(n))
    ans = [[0 for _ in range(3)] for _ in range(n)]
    for i in range(n):
        dummy = ''
        for j in range(n):
            dummy = dummy + lst[n - 1 - j][i]
        ans[i][0] = dummy

    for i in range(n):
        dummy = ''
        for j in range(n):
            dummy = dummy + lst[n - 1 - i][n - 1 - j]
        ans[i][1] = dummy

    for i in range(n):
        dummy = ''
        for j in range(n):
            dummy = dummy + lst[j][n - 1 - i]
        ans[i][2] = dummy

    print(f'#{case}')
    for i in ans:
        print(*i)
