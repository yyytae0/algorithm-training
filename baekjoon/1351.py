def check(a):
    if not a:
        return 1
    if dct.get(a):
        return dct[a]
    dct[a] = check(a//p) + check(a//q)
    return dct[a]


n, p, q = map(int, input().split())
dct = dict()
print(check(n))
