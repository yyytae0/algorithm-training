ip = int(input())

for case in range(1, ip+1):
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    lst.sort()
    dummy = 0
    for i in range(n):
        if lst[i][0] > i:
            dummy = lst[i][1]
        lst.pop(i)
