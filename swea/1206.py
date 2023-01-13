def make_map(n, lst):
    max = 0
    lst1 = list()

    for i in lst:
        if i > max:
            max = i

    for i in range(n):
        lst1.append([])
        for k in range(max):
            if k < lst[i]:
                lst1[i].append(1)

            else:
                lst1[i].append(0)

    return lst1, max

def check_view(n, lst, max):

    array = [[0] * max for _ in range(n)]

    for i in range(n):
        for j in range(max):
            if lst[i][j] == 1:
                if i < 2:
                    if lst[i+1][j] == 0:
                        if lst[i+2][j] == 0:
                            array[i][j] = 1
                        else:
                            continue
                    else:
                        continue

                elif i > n - 3:
                    if lst[i-1][j] == 0:
                        if lst[i-2][j] == 0:
                            array[i][j] = 1
                        else:
                            continue
                    else:
                        continue

                else:
                    if lst[i-1][j] == 0 and lst[i+1][j] == 0:
                        if lst[i-2][j] == 0 and lst[i+2][j] == 0:
                            array[i][j] = 1
                        else:
                            continue
                    else:
                        continue

            else:
                continue

    return array


ip = 10

for i in range(1, ip+1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst1, max = make_map(n, lst)
    lst2 = check_view(n, lst1, max)
    ans = 0
    for j in lst2:
        a = j.count(1)
        ans += a
    print("#%d %d" %(i, ans))
