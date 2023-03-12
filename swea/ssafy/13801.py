for case in range(1, 11):
    n, m = input().split()
    n = int(n)
    m = list(map(int, m))
    while True:
        cnt = 0
        for i in range(n-1):
            cnt += 1
            if m[i] != -1:
                idx = i + 1
                while m[idx] == -1:
                    idx = idx + 1
                    if idx > n - 1:
                        break
                if idx > n - 1:
                    continue
                if m[i] == m[idx]:
                    m[i], m[idx] = -1, -1
                    cnt -= 1
        if cnt == n-1:
            break
    ans = 0
    for i in m:
        if i != -1:
            ans = ans * 10 + i

    print(f'#{case} {ans}')
