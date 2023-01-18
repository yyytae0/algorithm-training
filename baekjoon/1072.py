def check(a, b):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != b[i][j]:
                if (i+2) >= len(a) or (j+2) >= len(a[0]):
                    return -1

                else:
                    cnt += 1
                    for k in range(3):
                        for l in range(3):
                            a[i + k][j + l] = str(1 - int(a[i + k][j + l]))

    if a == b:
        return cnt

    else:
        return -1


ip = list(map(int, input().split()))
a = []
b = []

for i in range(ip[0]):
    lst = list(input())
    a.append(lst)

for i in range(ip[0]):
    lst = list(input())
    b.append(lst)


if a == b:
    print(0)

elif ip[0] < 3 or ip[1] < 3:
    print(-1)

else:
    ans = check(a, b)
    print(ans)
