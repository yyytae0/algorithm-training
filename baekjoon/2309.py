lst = list()
total = 0
for i in range(9):
    dummy = int(input())
    lst.append(dummy)
    total = total + dummy

remove_lst = []
for i in range(9):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == total - 100:
            remove_lst.append(lst[i])
            remove_lst.append(lst[j])
            break

    if len(remove_lst) != 0:
        break

lst.remove(remove_lst[0])
lst.remove(remove_lst[1])
lst.sort()
for i in lst:
    print(i)
