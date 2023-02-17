from sys import stdin


ip = int(stdin.readline())

for _ in range(ip):
    n = int(stdin.readline())
    lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
    lst.sort()
    ans = 1
    dummy = lst[0][1]
    for i in range(1, n):
        if lst[i][1] < dummy:
            ans += 1
            dummy = lst[i][1]

    print(ans)
