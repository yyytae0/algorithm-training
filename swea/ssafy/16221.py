ip = int(input())

for i in range(1, ip+1):
    d, a, b, f = map(int, input().split())
    total = 0
    r = 1
    while d > 10**(-15):
        if r == 1:
            t = (d / (f + b))

        else:
            t = (d / (f + a))

        total = total + t * f
        d = d - a * t - b * t
        r = 1 - r

    print(f'#{i} {total}')
