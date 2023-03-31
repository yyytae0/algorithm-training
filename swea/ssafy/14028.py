def check():
    for i in range(len(thr)):
        lstb[int(thr[i])] = 0
        for j in range(m):
            if lstb[j]:
                t = int(thr[0:i] + str(j) + thr[i+1:], m)
                if t in lst:
                    return t
        lstb[int(thr[i])] = 1


ip = int(input())

for case in range(1, ip+1):
    n, m = 2, 3
    bi = input()
    thr = input()
    lsta = [1 for _ in range(n)]
    lstb = [1 for _ in range(m)]
    lst = []
    for i in range(len(bi)):
        lsta[int(bi[i])] = 0
        for j in range(n):
            if lsta[j]:
                t = int(bi[0:i] + str(j) + bi[i+1:], n)
                lst.append(t)
        lsta[int(bi[i])] = 1
    ans = check()
    print(f'#{case} {ans}')
