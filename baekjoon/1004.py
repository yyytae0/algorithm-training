def check(lst, x):
    length = (((lst[0] - x[0])**2) + ((lst[1] - x[1])**2))**(1/2)
    if length < lst[2]:
        return 1

    else:
        return 0


ip = int(input())

for i in range(ip):
    lst = list(map(int, input(). split()))
    me = lst[0:2]
    to = lst[2:4]
    n = int(input())
    planet = []
    for j in range(n):
        dummy = list(map(int, input().split()))
        planet.append(dummy)

    cnt = 0
    for j in planet:
        a = check(j, me)
        b = check(j, to)
        if a == 1 and b == 1:
            continue

        elif a == 0 and b == 0:
            continue

        else:
            cnt += 1

    print(cnt)
