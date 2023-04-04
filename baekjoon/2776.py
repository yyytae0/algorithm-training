def check(t):
    s = 0
    e = n-1
    while s < e:
        mid = (s+e)//2
        if lst[mid] == t:
            return 1
        if lst[mid] > t:
            e = mid-1
        else:
            s = mid+1
    if lst[s] == t or lst[e] == t:
        return 1
    return 0


ip = int(input())

for case in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())
    target = list(map(int, input().split()))
    lst.sort()
    for t in target:
        print(check(t))