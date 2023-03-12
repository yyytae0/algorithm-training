ip = int(input())

for case in range(1, ip+1):
    dummy = input()
    lst = list(map(str, input().split()))
    dct = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    for i in lst:
        dct[i] += 1

    print(f'#{case}')
    for i in dct.keys():
        for j in range(dct[i]):
            print(i, end=' ')
    print()
