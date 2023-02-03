def check(lst):
    chk = lst[0][0]
    for i in range(n):
        for j in range(n):
            if lst[i][j] == chk:
                continue
            else:
                return False

    return True


def cut(lst, start, last):
    if n == 1:
        return 1

    elif check(lst):
        return 1

    else:
        n = n//2
        cut(lst, start, last)


ip = int(input())
lst = list()
for i in range(ip):
    lst.append(list(map(int, input().split())))

