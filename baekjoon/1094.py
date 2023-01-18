def check(x, my):
    my_new = my[:]
    if sum(my) > x:
        my_new.remove(my[0])
        dummy = my[0]
        new = dummy/2
        my_new.append(new)
        if sum(my_new) == x:
            return len(my_new)

        else:
            if sum(my_new) < x:
                my_new.append(new)

            my_new.sort()
            return check(x, my_new)


ip = int(input())
my = [64]

if ip == 64:
    print(1)

else:
    a = check(ip, my)
    print(a)
