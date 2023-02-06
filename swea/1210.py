for i in range(10):
    case = int(input())
    lst = list(list(map(int, input().split())) for _ in range(100))
    idx = lst[-1].index(2)
    for j in range(99, -1, -1):
        if idx == 0:
            if lst[j][idx + 1] == 1:
                while lst[j][idx + 1]:
                    idx += 1
                    if idx == 99:
                        break

        elif lst[j][idx-1] == 1:
            while lst[j][idx-1]:
                idx -= 1
                if idx == 0:
                    break

        elif idx == 99:
            continue

        elif lst[j][idx+1] == 1:
            while lst[j][idx+1]:
                idx += 1
                if idx == 99:
                    break

    print(f'#{case} {idx}')
