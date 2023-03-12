ip = int(input())

for case in range(1, ip+1):
    n, a = input().split()
    lst = ['' for _ in range(int(n))]
    for idx, i in enumerate(a):
        if i.isdigit():
            d = int(i)
        else:
            d = ord(i)-55
        binary = bin(d)[2:]
        while len(binary) < 4:
            binary = '0' + binary
        lst[idx] = binary
    print(f'#{case}', ''.join(lst))
