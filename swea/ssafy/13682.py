for case in range(1, 11):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(100))
    for i in range(100):
        if lst[-1][i] == 2:
            idx = i
            break

    for i in range(99, -1, -1):
        if idx == 99:
            while lst[i][idx-1] == 1:
                idx -= 1
                if idx == -1:
                    break

        elif idx == 0:
            while lst[i][idx+1] == 1:
                idx += 1
                if idx == 99:
                    break

        else:
            if lst[i][idx+1] == 1:
                while lst[i][idx+1] == 1:
                    idx += 1
                    if idx == 99:
                        break

            elif lst[i][idx-1] == 1:
                while lst[i][idx-1] == 1:
                    idx -= 1
                    if idx == 0:
                        break

    print(f'#{case} {idx}')
