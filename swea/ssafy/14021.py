def in_order(a):
    if lst[a]:
        return
    if a*2 <= n:
        in_order(a*2)
        lst[a] += lst[a*2]
    if a*2+1 <= n:
        in_order(a*2+1)
        lst[a] += lst[a*2+1]


ip = int(input())

for case in range(1, ip+1):
    n, m, l = map(int, input().split())
    lst = [0 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a] = b
    in_order(1)
    print(f'#{case} {lst[l]}')
