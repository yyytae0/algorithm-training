ip = int(input())
id_lst = list()
check_lst = list()

for i in range(ip):
    id_ = list(input())
    id_lst.append(id_)

for i in range(1, len(id_lst[0])+1):
    for j in id_lst:
        if j[-i:] in check_lst:
            check_lst = list()
            break

        else:
            check_lst.append(j[-i:])

    if len(check_lst) > 0:
        print(i)
        break
