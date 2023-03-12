def check(num):
    a = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1],
         [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]
    for i in range(10):
        if num == a[i]:
            return i


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input())) for _ in range(n))
    code = 0
    for i in range(n):
        for j in range(m):
            if lst[i][j]:
                code = i
                break
        else:
            continue
        break
    idx = 0
    for i in range(m-1, -1, -1):
        if lst[code][i] == 1:
            idx = i
            break
    ans = []
    for i in range(8):
        num = []
        for j in range(7):
            num = [lst[code][idx]] + num
            idx -= 1
        s = check(num)
        ans = [s] + ans
    total = 0
    for i in range(0, 7, 2):
        total += ans[i]*3
    for i in range(1, 7, 2):
        total += ans[i]
    total += ans[7]
    if total % 10:
        print(f'#{case} 0')
    else:
        print(f'#{case} {sum(ans)}')