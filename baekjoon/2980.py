n, l = map(int, input().split())
lst = [[] for _ in range(1001)]
for _ in range(n):
    d, r, g = map(int, input().split())
    lst[d] = [r, g]
t = 0
now = 0
while now < l:
    if lst[now]:
        if t % (lst[now][0]+lst[now][1]) < lst[now][0]:
            t += 1
            continue
    t += 1
    now += 1
print(t)
