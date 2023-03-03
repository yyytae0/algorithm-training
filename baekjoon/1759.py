def solv(a, cnt):
    global ans
    if cnt == n-1:
        if d[0] >= 1 and d[1] >= 2:
            print(''.join(ans))
        return

    for i in range(a+1, m):
        t = lst[i]
        if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
            d[0] += 1
        else:
            d[1] += 1
        ans.append(t)
        solv(i, cnt+1)
        ans.pop()
        if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
            d[0] -= 1
        else:
            d[1] -= 1


n, m = map(int, input().split())
lst = list(input().split())
lst.sort()
for i in range(m):
    d = [0, 0]
    t = lst[i]
    if t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u':
        d[0] += 1
    else:
        d[1] += 1
    ans = [t]
    solv(i, 0)
