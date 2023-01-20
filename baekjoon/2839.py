def check(n, cnt):
    if n % 5 == 0:
        cnt = cnt + n//5

    elif n < 3:
        cnt = -1

    else:
        n = n - 3
        cnt = cnt + 1
        cnt = check(n, cnt)

    return cnt


ip = int(input())

a = check(ip, 0)
print(a)
