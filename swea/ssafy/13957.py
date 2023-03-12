for i in range(10):
    case = int(input())
    lst = list(map(int, input().split()))
    idx = 0
    cnt = 1
    ans = []
    while True:
        lst[idx] -= cnt
        if lst[idx] <= 0:
            lst[idx] = 0
            idx = (idx + 1) % 8
            break
        idx = (idx+1) % 8
        cnt += 1
        if cnt == 6:
            cnt = 1
    for i in range(8):
        ans.append(lst[idx])
        idx = (idx + 1) % 8
    print(f'#{case}', *ans)
