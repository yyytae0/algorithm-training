ip = int(input())

for i in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    small = 1000000
    big = 0
    for j in range(n-m+1):
        dummy = 0
        for k in range(m):
            dummy = dummy + lst[j+k]

        if dummy > big:
            big = dummy

        if dummy < small:
            small = dummy

    print(f'#{i} {big-small}')
