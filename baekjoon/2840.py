n, k = map(int, input().split())
hint = list(list(input().split()) for _ in range(k))
lst = ['?' for _ in range(n)]
now = 0
ans = 0
dct = dict()
while hint:
    h = hint.pop()
    if lst[now] != '?' and lst[now] != h[1]:
        ans = '!'
        break
    if lst[now] == '?':
        lst[now] = h[1]
        if h[1] in dct.keys():
            ans = '!'
            break
        dct[h[1]] = 1
    now = (now + int(h[0])) % n
if ans:
    print(ans)
else:
    print(''.join(lst))
