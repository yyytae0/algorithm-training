def check(n, cnt):
    if n == 1:
        return 1
    return check(n-1, cnt+1)*(n-cnt)


ip = int(input())
print(check(ip, 0))
