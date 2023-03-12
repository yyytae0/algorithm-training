ip = int(input())

for case in range(1, ip+1):
    a = input()
    new = ''
    for i in a:
        if i.isdigit():
            d = int(i)
        else:
            d = ord(i)-55
        dummy = bin(d)[2:]
        new += '0' * (4-len(dummy)) + dummy

    code = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4,
            '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

    idx = 4*len(a)-1
    while new[idx] != '1':
        idx -= 1
    ans = []
    while new[idx] == '1':
        ans.append(code[new[idx-5:idx+1]])
        idx -= 6
        if idx < 0:
            break
    ans.reverse()
    print(f'#{case}', *ans)
