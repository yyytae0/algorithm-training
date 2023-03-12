for case in range(1, 11):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(100))
    mn = 10000
    for i in range(100):
        if lst[0][i] == 1:
            idx = i
            cnt = 0
            for j in range(100):
                if idx == 99:
                    while lst[j][idx - 1] == 1:
                        idx -= 1
                        cnt += 1
                        if idx == -1:
                            break

                elif idx == 0:
                    while lst[j][idx + 1] == 1:
                        idx += 1
                        cnt += 1
                        if idx == 99:
                            break

                else:
                    if lst[j][idx + 1] == 1:
                        while lst[j][idx + 1] == 1:
                            idx += 1
                            cnt += 1
                            if idx == 99:
                                break

                    elif lst[j][idx - 1] == 1:
                        while lst[j][idx - 1] == 1:
                            idx -= 1
                            cnt += 1
                            if idx == 0:
                                break

            if cnt < mn:
                mn = cnt
                mn_idx = i

    print(f'#{case} {mn_idx}')
