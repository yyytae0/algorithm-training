def check(a, b):
    sum = 0
    for i in range(a, a+m):
        for j in range(b, b+m):
            sum += lst[i][j]
    return sum


ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(map(int, input().split())) for _ in range(n))
    mx = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            dummy = check(i, j)
            if dummy > mx:
                mx = dummy

    print(f'#{case} {mx}')
