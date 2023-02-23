n = int(input())
me = int(input())
if n == 1:
    print(0)
else:
    lst = list(int(input()) for _ in range(n - 1))
    cnt = 0
    while True:
        lst.sort()
        if lst[-1] >= me:
            lst[-1] -= 1
            me += 1
            cnt += 1
        else:
            break
    print(cnt)
