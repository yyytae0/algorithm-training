ip = int(input())

for case in range(1, ip+1):
    a = input()
    cnt = 6
    num = 0
    ans = []
    for i in a:
        num = num + (2**cnt)*int(i)
        cnt -= 1
        if cnt < 0:
            ans.append(num)
            num = 0
            cnt = 6
    print(f'#{case}', *ans)