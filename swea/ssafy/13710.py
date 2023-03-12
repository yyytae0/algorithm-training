for _ in range(10):
    case = int(input())
    target = input()
    n_t = len(target)
    ip = input()
    n_ip = len(ip)
    dummy = 0
    cnt = 0
    for i in range(n_ip - n_t + 1):
        if ip[i] == target[0]:
            for j in range(n_t):
                if ip[i+j] == target[j]:
                    dummy = 1

                else:
                    dummy = 0
                    break
            if dummy == 1:
                cnt += 1

    print(f'#{case} {cnt}')
