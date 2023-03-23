import math
from sys import stdin


def check():
    cnt = 0
    for i in lst:
        cnt += math.ceil(i/mid)
        if cnt > n:
            return False
    return True


n, m = map(int, stdin.readline().split())
lst = list(int(stdin.readline()) for _ in range(m))
s, g = 1, max(lst)
while s != g:
    mid = (s+g)//2
    if check():
        g = mid
    else:
        s = mid + 1
print(s)
