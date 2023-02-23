lst = list(int(input()) for _ in range(10))
now, dummy = 0, 0
for i in lst:
    dummy = now
    now += i
    if now > 100:
        break

if abs(100-dummy) < abs(100-now):
    print(dummy)
else:
    print(now)
