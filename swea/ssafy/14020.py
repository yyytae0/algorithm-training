def in_order(a):
    global ans
    if 0 < a <= n:
        in_order(2 * a)
        ans += lst[a]
        in_order(2 * a + 1)


for case in range(1, 11):
    n = int(input())
    lst = ['' for _ in range(n+1)]
    dct = dict()
    ans = ''
    visit = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        dummy = list(input().split())
        dct[i] = dummy[1:]
        dct[i].pop(0)
        dct[i] = list(map(int, dct[i]))
        lst[i] = dummy[1]
    in_order(1)
    print(f'#{case} {ans}')