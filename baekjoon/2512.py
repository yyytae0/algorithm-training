n = int(input())
lst = list(map(int, input().split()))
t = int(input())
s, g = 0, max(lst)
while s != g:
    total = 0
    mid = (s + g)//2
    for i in lst:
        if i <= mid:
            total += i
        else:
            total += mid
    if total >= t:
        g = mid
    else:
        s = mid+1
total = 0
mid = (s + g)//2
for i in lst:
    if i <= mid:
        total += i
    else:
        total += mid
if total > t:
    print(s-1)
else:
    print(s)
