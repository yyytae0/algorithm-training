def change(n):
    ans = 0
    while n:
        d = n % 10
        n = n//10
        ans += d**p
    return ans


a, p = map(int, input().split())
dct = dict()
d = a
cnt = 1
dct[d] = 1
while True:
    cnt += 1
    d = change(d)
    try:
        dct[d]
    except KeyError:
        dct[d] = cnt
    else:
        ans = dct[d] - 1
        break

print(ans)
