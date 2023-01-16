def make_web(lst):




ip = int(input())

for i in range(1, ip + 1):
    n = int(input())
    lst_web = list()
    lst_remain = list()
    for j in range(n):
        if j < 3:
            lst = list(map(int, input().split()))
            lst_web.append(lst)

        else:
            lst = list(map(int, input().split()))
            lst_remain.append(lst)

    a = len(lst_remain)
    web = make_web(lst_Web)

    for j in range(a):
        ans = check()
