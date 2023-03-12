ip = int(input())

for case in range(1, ip+1):
    a = input()
    cnt = 0
    for i in a:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        ans = 1
    else:
        ans = 0
    print(f'#{case} {ans}')
