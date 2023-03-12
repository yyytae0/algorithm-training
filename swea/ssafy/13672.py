

ip = int(input())

for i in range(1, ip+1):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    num, now, a, b, start, last = 1, 1, 0, 0, 0, n-1

    while True:
        lst[b][a] = num
        num += 1
        if num == n**2 + 1:
            break

        if now == 1:
            if a == last:
                now = 2
                b += 1
            else:
                a += 1

        elif now == 2:
            if b == last:
                now = 3
                a -= 1
            else:
                b += 1

        elif now == 3:
            if a == start:
                now = 4
                b -= 1
            else:
                a -= 1

        elif now == 4:
            if b == start+1:
                now = 1
                a += 1
                start += 1
                last -= 1
            else:
                b -= 1

    print(f'#{i}')
    for j in lst:
        print(*j)
