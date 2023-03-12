def check(n):
    lst = [0] * 5
    cnt = 0
    if n % 2 == 0:
        while n % 2 == 0:
            n = n//2
            cnt += 1
        lst[0] = cnt
        cnt = 0

    if n % 3 == 0:
        while n % 3 == 0:
            n = n // 3
            cnt += 1
        lst[1] = cnt
        cnt = 0

    if n % 5 == 0:
        while n % 5 == 0:
            n = n//5
            cnt += 1
        lst[2] = cnt
        cnt = 0

    if n % 7 == 0:
        while n % 7 == 0:
            n = n//7
            cnt += 1
        lst[3] = cnt
        cnt = 0

    if n % 11 == 0:
        while n % 11 == 0:
            n = n//11
            cnt += 1
        lst[4] = cnt

    return lst


ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    ans = check(n)
    print(f'#{i}', *ans)
