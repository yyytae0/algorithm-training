def check(lst, find):
    target = find.pop(0)
    cnt = 0

    if lst.index(target) >= len(lst)/2:
        cnt = len(lst) - lst.index(target)
        lst_new = lst[lst.index(target)+1:]+lst[:lst.index(target)]

    else:
        cnt = lst.index(target)
        lst_new = lst[lst.index(target) + 1:] + lst[:lst.index(target)]

    return lst_new, find, cnt


ip = list(map(int, input().split()))
lst_origin = list(range(1, ip[0]+1))
find = list(map(int, input().split()))
total = 0
for i in range(len(find)):
    lst_origin, find, cnt = check(lst_origin, find)
    total = total + cnt
print(total)
