ip = int(input())

for case in range(1, ip+1):
    n = float(input())
    ans = ''
    cnt = 1
    while n and cnt < 13:
        if n >= 2**(-cnt):
            n -= 2**(-cnt)
            ans += '1'
        else:
            ans += '0'
        cnt += 1

    if n:
        print(f'#{case} overflow')
    else:
        print(f'#{case} {ans}')
