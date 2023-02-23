def check():
    if now[2] == k:
        return now[0], now[1]
    if k > now[2] + r - 1:
        now[1] += r-1
        now[2] += r-1
        if now[2] == k:
            return now[0], now[1]
    else:
        for i in range(r - 1):
            now[1] += 1
            now[2] += 1
            if now[2] == k:
                return now[0], now[1]
    if k > now[2] + c - 1:
        now[0] += c-1
        now[2] += c-1
        if now[2] == k:
            return now[0], now[1]
    else:
        for i in range(c - 1):
            now[0] += 1
            now[2] += 1
            if now[2] == k:
                return now[0], now[1]
    if k > now[2] + r - 1:
        now[1] -= r-1
        now[2] += r-1
        if now[2] == k:
            return now[0], now[1]
        for i in range(c - 1):
            now[0] -= 1
            now[2] += 1
            if now[2] == k:
                return now[0], now[1]
    else:
        for i in range(r - 1):
            now[1] -= 1
            now[2] += 1
            if now[2] == k:
                return now[0], now[1]


c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
else:
    now = [1, 1, 1]
    while k > now[2] + 2 * r + 2 * c - 4:
        now = [now[0] + 1, now[1] + 1, now[2] + 2 * r + 2 * c - 4]
        r -= 2
        c -= 2
    print(*check())
