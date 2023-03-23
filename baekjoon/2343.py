def check():
    cnt = 1
    now = 0
    for i in lst:
        if i > mid:
            return True
        now += i
        if now > mid:
            now = i
            cnt += 1
    if cnt > m:
        return True
    return False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
g = max(lst)*(n//m+1)
s = 0

while s != g:
    mid = (s+g)//2
    if check():
        s = mid + 1
    else:
        g = mid
mid = (s+g)//2
if check():
    print(s+1)
else:
    print(s)
