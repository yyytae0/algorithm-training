ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    q = list()
    cnt = 0
    num = 1
    for i in lst:
        while cnt == n:
            now = [q[0][0]//2, q[0][1]]
            del q[0]
            if now[0]:
                q.append(now)
            else:
                cnt -= 1
        q.append([i, num])
        cnt += 1
        num += 1
    while q:
        now = [q[0][0] // 2, q[0][1]]
        del q[0]
        if now[0]:
            q.append(now)
    print(f'#{case} {now[1]}')

