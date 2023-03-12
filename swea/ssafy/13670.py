ip = int(input())

for i in range(1, ip+1):
    lst = list(map(int, input().split()))
    dummy = list()
    ans = 0
    for j in range(1 << 10):
        for k in range(10):
            if j & (1 << k):
                dummy.append(lst[k])

        if dummy:
            if sum(dummy) == 0:
                print(f'#{i} 1')
                ans = 1
                break
            dummy = []

        if ans == 1:
            break

    if ans == 0:
        print(f'#{i} 0')
