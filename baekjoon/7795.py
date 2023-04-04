def check(i):
    global ans
    s = 0
    e = m-1
    while s < e:
        mid = (s+e)//2
        if b[mid] >= i:
            e = mid-1
        else:
            s = mid+1
    ans += (s+e)//2 + 1


ip = int(input())

for case in range(ip):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    ans = 0
    for i in a:
        if i <= b[0]:
            continue
        elif i > b[-1]:
            ans += m
        else:
            check(i)
    print(ans)