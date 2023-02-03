k, n = map(int, input().split())
lst = list()
for i in range(k):
    lst.append(int(input()))

ans = max(lst)
start = 1
last = 2 ** 31 - 1
while True:
    cnt = 0
    for i in lst:
        cnt += i//ans

    if cnt >= n:
        start = ans
        ans = (start + last)//2

    else:
        last = ans
        ans = (start + last)//2

    if last - start < 50:
        break

for i in range(start, last+2):
    cnt = 0
    for j in lst:
        cnt += j//i

    if cnt < n:
        print(i-1)
        break
