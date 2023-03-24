def check():
    cnt = 0
    for i in lst:
        for j in i:
            if j >= mid:
                cnt += mid
            else:
                cnt += j
            if cnt >= total//2 + total%2:
                return True
    return False


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
s, g = 1, 1
total = 0
for i in lst:
    for j in i:
        total += j
        if j > g:
            g = j
if total == 0:
    print(0)
else:
    while s != g:
        mid = (s + g) // 2
        if check():
            g = mid
        else:
            s = mid + 1
    print(s)
