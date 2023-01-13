def rest(ship, colony, cnt):
    if colony[0] == None:
        return cnt

    elif sum(colony) < ship:
        return cnt

    lst1 = colony.sort()
    a = len(lst1)

    total = ship
    for i in range(a):
        total = total + lst1[i]
        if i < len(colony):
            if total < colony[i+1]:
                cnt = -1
                return cnt

    lst2 = colony.sort(reverse = True)
    ship_now = ship

    for i in lst2:
        if i < ship_now:
            ship_now = ship + i
            cnt += 1
            lst2.remove(i)
            rest(ship_now, lst2)

    return cnt


ip = int(input())

for i in range(1, ip+1):
    lst = list(map(int, input().split()))
    ship = lst[1]
    lst2 = list(map(int, input().split()))
    a = rest(ship, lst2, 0)
    print(0)
