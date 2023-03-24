from sys import stdin


def check():
    cnt = 0
    for i in lst:
        if i < mid:
            cnt += mid-i
            if cnt > k:
                return True
    return False


n, k = map(int, stdin.readline().split())
lst = list(int(stdin.readline()) for _ in range(n))
s, g = min(lst), max(lst)+k
while s != g:
    mid = (s+g)//2
    if check():
        g = mid
    else:
        s = mid+1
mid = s
if check():
    print(s-1)
else:
    print(s)
