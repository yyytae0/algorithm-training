ip = int(input())
t, cnt, y, x = 2, 5, 2, 1
while True:
    t = t + cnt
    if t > ip:
        t = t - cnt
        break
    cnt += 4
    y += 2
if ip == 1:
    print('1/1')
if t == ip:
    print(f'{x}/{y}')
else:
    if ip <= t + y - 1:
        d = y
        for i in range(d - 1):
            t += 1
            y -= 1
            x += 1
            if t == ip:
                print(f'{x}/{y}')
                break
    else:
        t = t + y
        x = y + 1
        y = 1
        d = x
        if t == ip:
            print(f'{x}/{y}')

        else:
            for i in range(d - 1):
                t += 1
                y += 1
                x -= 1
                if t == ip:
                    print(f'{x}/{y}')
