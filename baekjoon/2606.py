def check(lst, a):
    new_lst = lst[:]
    for i in lst:
        if (i[0] in a) or (i[1] in a):
            a = a.union({i[0], i[1]})
            new_lst.remove(i)
            a = check(new_lst, a)

    return a


ip = int(input())
n = int(input())
lst = list()

for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        lst.append([a, b])

    else:
        lst.append([b, a])

lst.sort()

a = {1}
ans = check(lst, a)

print(len(ans)-1)
