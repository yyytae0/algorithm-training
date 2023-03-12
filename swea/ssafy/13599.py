def my_max(*args):
    big = 0
    for i in args:
        if i > big:
            big = i

    return big


for i in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for j in range(2, n-2):
        if lst[j] > my_max(lst[j-2], lst[j-1], lst[j+1], lst[j+2]):
            cnt += lst[j] - my_max(lst[j-2], lst[j-1], lst[j+1], lst[j+2])

    print(f'#{i} {cnt}')
