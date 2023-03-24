def check():
    cnt = 0
    for i in lst:
        cnt += mid//i
        if cnt >= m:
            return True
    return False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
s, g = 1, min(lst)*m
while s != g:
    mid = (s+g)//2
    if check():
        g = mid
    else:
        s = mid + 1
print(s)
