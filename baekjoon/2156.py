from sys import stdin

ip = int(input())
lst = list()
for i in range(ip):
    lst.append(int(stdin.readline()))

if ip > 2:
    ans = list([0, 0, 0, 0] for _ in range(ip))
    ans[0][1] = lst[0]
    ans[1][0] = lst[0]
    ans[1][1] = lst[1]
    ans[1][2] = lst[0] + lst[1]

    for i in range(2, ip):
        ans[i][0] = max(ans[i-1])
        ans[i][1] = ans[i - 1][0] + lst[i]
        ans[i][2] = ans[i - 1][1] + lst[i]
        ans[i][3] = ans[i - 1][2]

    print(max(ans[-1]))

elif ip == 2:
    print(lst[0]+lst[1])

elif ip == 1:
    print(lst[0])
