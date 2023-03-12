def check():
    dummy = 0
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '#':
                a, b = i, j
                dummy = 1
                break
        if dummy:
            break

    for y in range(a, a + int(cnt ** (1 / 2))):
        for x in range(b, b + int(cnt ** (1 / 2))):
            if 0 <= y <= n - 1 and 0 <= x <= n - 1:
                if lst[y][x] == '#':
                    continue
                else:
                    return 'no'
            else:
                return 'no'
    return 'yes'


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(input()) for _ in range(n))
    t = []
    for i in range(1, 21):
        t.append(i**2)
    cnt = 0
    for i in lst:
        for j in i:
            if j == '#':
                cnt += 1

    if cnt not in t:
        print(f'#{case} no')
    else:
        ans = check()
        print(f'#{case} {ans}')
