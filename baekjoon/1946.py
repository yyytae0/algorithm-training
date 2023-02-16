from sys import stdin


ip = int(stdin.readline())

for _ in range(ip):
    n = int(stdin.readline())
    lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
    lst.sort(reverse=True)
    ans = 1
    dummy = 0
    for i in range(n):
        if dummy == 1:
            for j in range(i + 1, n):
                if lst[i][1] > lst[j][1]:
                    ans -= 1
                    break
            ans += 1
        if lst[i][1] == 1:
            dummy = 1

    print(ans)
