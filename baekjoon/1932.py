ip = int(input())
lst = list()

for i in range(ip):
    lst.append(list(map(int, input().split())))

for i in range(1, len(lst)):
    for j in range(len(lst[i])):
        if j == 0:
            lst[i][0] = lst[i][0] + lst[i-1][0]

        elif j == (len(lst[i])-1):
            lst[i][j] = lst[i][j] + lst[i-1][j-1]

        else:
            lst[i][j] = max(lst[i][j]+lst[i-1][j-1], lst[i][j]+lst[i-1][j])

print(max(lst[ip-1]))
