def check():
    cnt = 0
    for i in lst:
        cnt += i//mid
        if cnt >= n:
            return True
    return False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
s, g = 1, max(lst)
mid = 1
if check():
    while s != g:
        mid = (s + g) // 2
        if check():
            s = mid + 1
        else:
            g = mid
    mid = s
    if check():
        print(s)
    else:
        print(s - 1)
else:
    print(0)
