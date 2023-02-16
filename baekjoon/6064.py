ip = int(input())

for case in range(1, ip+1):
    m, n, x, y = map(int, input().split())
    a, b = 1, 1
    cnt = x
    a, b = x, b+x-a
    while b > n:
        b -= n
    while True:
        if b == y:
            print(cnt)
            break
        if cnt > m*n:
            print(-1)
            break

        cnt += m
        b = b + m
        while b > n:
            b -= n
