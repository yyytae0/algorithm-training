n = int(input())
for i in range(n):
    dict_a = {1: 0, 2: 0, 3: 0, 4: 0}
    dict_b = {1: 0, 2: 0, 3: 0, 4: 0}
    lst_a = list(map(int, input().split()))[1:]
    lst_b = list(map(int, input().split()))[1:]
    for j in lst_a:
        dict_a[j] += 1

    for j in lst_b:
        dict_b[j] += 1

    dummy = 0
    for j in range(4, 0, -1):
        if dict_a[j] != dict_b[j]:
            dummy = 1
            if dict_a[j] > dict_b[j]:
                print('A')

            else:
                print('B')
            break

    if dummy == 0:
        print('D')
