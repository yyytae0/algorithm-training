ip = int(input())

for case in range(1, ip+1):
    target = list(input())
    n = len(target)
    ans = n
    while True:
        dummy = 0
        for i in range(n - 1):
            dummy += 1
            if target[i]:
                idx = i + 1
                while not target[idx]:
                    idx += 1
                    if idx > n - 1:
                        break
                if idx > n-1:
                    continue
                if target[i] == target[idx]:
                    target[i] = 0
                    target[idx] = 0
                    ans -= 2
                    dummy -= 1
        if dummy == n-1:
            break

    print(f'#{case} {ans}')
