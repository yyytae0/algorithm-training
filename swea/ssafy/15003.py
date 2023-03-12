ip = int(input())

for case in range(1, ip+1):
    m = input()
    dummy = 0
    cnt = 0
    for i in m:
        if int(i) != dummy:
            cnt += 1
            dummy = 1 - dummy
        else:
            continue
    print(f'#{case} {cnt}')
