ip = list(map(int, input().split()))
lst = list()
max = 1

for i in range(ip[0]):
    line = input()
    lst.append(line)

for i in range(ip[0] - 1):
    for j in range(ip[1]):
        for k in range(j+1, ip[1]):
            if i+k-j >= ip[0]:
                break

            elif lst[i][j] == lst[i][k] and lst[i][j] == lst[i+k-j][j] and lst[i][j] == lst[i+k-j][k]:
                if ((k-j+1)**2) > max:
                    max = ((k-j+1)**2)
                    continue

print(max)
