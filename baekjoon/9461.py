def check(n):
    lst = [0]*101
    lst[1] = 1
    lst[2] = 1
    lst[3] = 1
    lst[4] = 2
    lst[5] = 2
    lst[6] = 3
    lst[7] = 4
    lst[8] = 5
    for i in range(9, n+1):
        lst[i] = lst[i-1] + lst[i-5]

    return lst


lst = check(100)
ip = int(input())
for i in range(ip):
    n = int(input())
    print(lst[n])
