ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input())) for _ in range(n))
    ans = 0
    for i in range(n//2):
        for j in range(n//2-i, n//2+i+1):
            ans += lst[i][j]
    for i in range(n//2+1):
        for j in range(i, n-i):
            ans += lst[n//2 + i][j]
    print(f'#{case} {ans}')
