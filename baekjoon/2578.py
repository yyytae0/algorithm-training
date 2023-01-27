def check(n, lst):
    for i in range(5):
        for j in range(5):
            if lst[i][j] == n:
                lst[i][j] = 0
                return lst


def bingo(lst):
    cnt = 0
    for i in range(5):
        dummy = 0
        if lst[i][i] != 0:
            dummy = 1
            break

    if dummy == 0:
        cnt += 1

    for i in range(5):
        dummy = 0
        if lst[i][4-i] != 0:
            dummy = 1
            break

    if dummy == 0:
        cnt += 1

    for i in range(5):
        if lst[i] == [0, 0, 0, 0, 0]:
            cnt += 1

        if cnt == 3:
            return True

    for i in range(5):
        dummy = 0
        for j in range(5):
            if lst[j][i] != 0:
                dummy = 1
                break

        if dummy == 0:
            cnt += 1

        if cnt == 3:
            return True

    return False


lst = list()
for i in range(5):
    lst.append(list(map(int, input().split())))

num_lst = list()
for i in range(5):
    num_lst = num_lst + list(map(int, input().split()))

cnt = 0
for i in num_lst:
    cnt += 1
    lst = check(i, lst)
    if cnt >= 12:
        if bingo(lst):
            print(cnt)
            break
