ip = int(input())

for case in range(1, ip+1):
    a = list(input())
    stack = list()
    for i in range(len(a)):
        if a[i] == ')':
            if a[i-1] == '(':
                a[i-1] = ''
                a[i] = 'L'
    a = ''.join(a)
    cnt = 0
    ans = 0
    for i in a:
        if i == 'L':
            ans += cnt
        elif i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
            ans += 1
    print(f'#{case} {ans}')
