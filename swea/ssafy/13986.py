def check(a):
    global ans
    if dct[a]:
        for i in dct[a]:
            ans += 1
            check(i)
    else:
        return


ip = int(input())

for case in range(1, ip+1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    dct = dict()
    for i in range(1, e+2):
        dct[i] = []
    for i in range(e):
        dct[lst[2*i]].append(lst[2*i+1])
    ans = 1
    check(n)
    print(f'#{case} {ans}')
