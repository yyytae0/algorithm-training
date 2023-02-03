n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = max(lst)
start = 1
last = ans
while True:
    total = 0
    for i in lst:
        if i > ans:
            total = total + (i-ans)

    if total >= m:
        start = ans
        ans = (start+last)//2

    else:
        last = ans
        ans = (start+last)//2

    if last - start < 50:
        break

for i in range(start, last+2):
    total = 0
    for j in lst:
        if j > i:
            total = total + (j-i)

    if total < m:
        print(i-1)
        break
