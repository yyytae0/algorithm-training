n = int(input())
dct = dict()
for i in range(n-1):
    a, b = input().split()
    dct[a] = b

d1, d2 = input().split()
a, b = d1, d2
d = 1
while d:
    try:
        dct[a]
    except KeyError:
        d = 0
    else:
        if dct[a] == b:
            break
        else:
            a = dct[a]
if d:
    print(d)
else:
    a, b = d1, d2
    d = 1
    while d:
        try:
            dct[b]
        except KeyError:
            d = 0
        else:
            if dct[b] == a:
                break
            else:
                b = dct[b]
    print(d)
