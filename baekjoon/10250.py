ip = int(input())

for i in range(ip):
    h, w, n = map(int, input().split())
    cnt = 1
    while n > h:
        n -= h
        cnt += 1

    if cnt < 10:
        cnt = '0' + str(cnt)

    print(str(n)+str(cnt))
