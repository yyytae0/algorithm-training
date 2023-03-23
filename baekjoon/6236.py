def check():
    now = mid
    cnt = 1
    for i in lst:
        if i <= now:
            now -= i
        else:
            if i > mid:
                return False
            now = mid - i
            cnt += 1
    if cnt > m:
        return False
    else:
        return True


n, m = map(int, input().split())
lst = list(int(input()) for _ in range(n))
s, g = 0, max(lst)*(n//m+1)
while s != g:
    mid = (s+g)//2
    if check():
        g = mid
    else:
        s = mid + 1
print(s)
