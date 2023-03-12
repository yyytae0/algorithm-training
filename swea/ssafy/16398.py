ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    dummy = ''
    for i in range(n):
        a, b = input().split()
        for j in range(int(b)):
            dummy += a

    cnt = 0
    print(f'#{case}')
    for i in dummy:
        print(i, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()

