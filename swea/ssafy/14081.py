def in_order(a):
    global cnt
    if 0 < a <= n:
        in_order(2 * a)
        lst[a] = cnt
        cnt += 1
        in_order(2 * a + 1)


ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = [0 for _ in range(n+1)]
    cnt = 1
    in_order(1)
    print(f'#{case} {lst[1]} {lst[n//2]}')
