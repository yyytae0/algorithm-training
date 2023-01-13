def cnt_binary(n, k):
    cnt = n
    if n != 1:
        if n == 2 and k == 1:
            cnt = 4
        elif k == 1:
            cnt += 1
        elif k >= n:
            cnt *= 2

    return cnt




ip = int(input())

for i in range(1, ip+1):
    lst = list(map(int, input().split()))
    a = cnt_binary(lst[0], lst[1])
    print("#%d %d" % (i, a))
