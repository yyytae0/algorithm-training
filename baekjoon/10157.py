c, r = map(int, input().split())
k = int(input())

if k > c*r:
    print(0)

else:
    dummy = 1
    total = 0
    while True:
        if k > (c-dummy*2+2)*2 + (r-dummy*2+2)*2 - 4:
            k = k - ((c-dummy*2+2)*2 + (r-dummy*2+2)*2 - 4)
            total = total + (c-dummy*2+2)*2 + (r-dummy*2+2)*2 - 4
            dummy += 1
            pass

        else:
            break

    now = [dummy, dummy, total + 1]
    print(dummy)
    print(now)
    if k <= now[2] + r - 2*(dummy-1) - 1:
        now[1] = now[1] + k - now[2]

    elif k < now[2] + r - 2*(dummy-1) - 1 + c - 2*(dummy-1) - 1:
        now[1] = r - dummy
        now[0] = now[0] + k - (now[2] + r - 2*(dummy-1) - 1)

    elif k < now[2] + 2*(r - 2*(dummy-1) - 1) + c - 2*(dummy-1) - 1:
        now[0] = c - dummy
        now[1] =
        pass

    else:
        pass

