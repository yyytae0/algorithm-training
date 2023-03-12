ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    small = 1000000
    big = 0
    lst = list(map(int, input().split()))
    for j in lst:
        if j > big:
            big = j

        if j < small:
            small = j

    print(f'#{i} {big-small}')
