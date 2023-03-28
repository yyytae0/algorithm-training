def run(dct):
    for i in range(8):
        if dct[i]:
            if dct[i+1] and dct[i+2]:
                return 1
    return 0


def triplet(dct):
    for i in range(10):
        if dct[i] >= 3:
            return 1
    return 0


ip = int(input())

for case in range(1, ip+1):
    lst = list(map(int, input().split()))
    a = {}
    b = {}
    ans = 0
    for i in range(10):
        a[i] = 0
        b[i] = 0
    for i in range(6):
        a[lst[2*i]] += 1
        b[lst[2*i + 1]] += 1
        if run(a) or triplet(a):
            ans = 1
            break
        if run(b) or triplet(b):
            ans = 2
            break
    print(f'#{case} {ans}')
