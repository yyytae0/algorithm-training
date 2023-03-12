ip = int(input())

for case in range(1, ip+1):
    lst = []
    mx = 0
    for i in range(5):
        a = list(input())
        n = len(a)
        a = a + [''] * (15-n)
        lst.append(a)
        if n > mx:
            mx = n

    ans = ''
    for idx in range(mx):
        for i in lst:
            ans += i[idx]
    print(f'#{case} {ans}')
