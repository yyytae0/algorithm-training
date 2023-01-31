def tile(n):
    lst = [1] * 3
    for i in range(2, n+1):
        lst[0] = lst[1]%15746 + lst[2]%15746
        lst[2] = lst[1]
        lst[1] = lst[0]

    return lst[0]%15746


ip = int(input())
print(tile(ip))
