a, b, v = map(int, input().split())
step = a-b
now = 0
cnt = 0
while True:
    cnt += 1
    now = now + a
    if now >= v:
        print(cnt)
        break

    else:
        now = now - b
