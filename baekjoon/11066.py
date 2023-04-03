ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    sm = 0
    while True:
        now = 5000000
        idx_l, idx_r = 0, 0
        for i in range(n):
            if lst[i]:
                for j in range(i+1, n):
                    if lst[j]:
                        d = lst[i]+lst[j]
                        if d < now:
                            idx_l = i
                            idx_r = j
                            now = d
                        break
        if idx_r == 0:
            pass
        lst[idx_l] = now
        lst[idx_r] = 0
        sm += now

