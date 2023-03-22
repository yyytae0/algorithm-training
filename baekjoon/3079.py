from sys import stdin


def check():
    d = 0
    for i in lst:
        d += mid//i
    return d


n, m = map(int, stdin.readline().split())
lst = list(int(stdin.readline()) for _ in range(n))
s, g = 0, min(lst)*m
while s != g:
    mid = (s + g)//2
    d = check()
    if d >= m:
        g = mid
    else:
        s = mid+1
print(s)
