from sys import stdin


n = int(stdin.readline())
dct = dict()
mx_n, mx_name = 0, ''
for i in range(n):
    a = stdin.readline().strip()
    if dct.get(a):
        dct[a] += 1
    else:
        dct[a] = 1
    if dct[a] >= mx_n:
        if dct[a] == mx_n:
            if mx_name > a:
                mx_name = a
        else:
            mx_n = dct[a]
            mx_name = a
print(mx_name)
