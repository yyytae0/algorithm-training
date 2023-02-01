def check(lst, a):
    dummy = 0
    for i in lst:
        if (i[0] in a) or (i[1] in a):
            dummy = 1
            a = a.union({i[0], i[1]})
            lst.remove(i)
            break

    if dummy == 1:
        a = check(lst, a)

    return a


ip = int(input())
n = int(input())
lst = list()

for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

ans = {1}
ans = check(lst, ans)

print(len(ans)-1)
