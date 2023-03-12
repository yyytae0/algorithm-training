ip = int(input())

for case in range(1, ip+1):
    target = set(list(input()))
    dummy = input()
    dct = dict()
    for i in target:
        dct[i] = 0

    mx = 0
    for i in dummy:
        try:
            dct[i]
        except KeyError:
            continue
        else:
            dct[i] += 1
            if dct[i] > mx:
                mx = dct[i]

    print(f'#{case} {mx}')
