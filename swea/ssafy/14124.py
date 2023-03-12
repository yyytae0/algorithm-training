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

    cnt = 6
    num = 0
    ans = []
    for i in new:
        num = num + (2 ** cnt) * int(i)
        cnt -= 1
        if cnt < 0:
            ans.append(num)
            num = 0
            cnt = 6
    num = 0
    cnt = 0
    for i in range(4*len(a)%7):
        num = num + (2 ** cnt) * int(new[-i-1])
        cnt += 1
    ans.append(num)
    print(f'#{case}', *ans)
