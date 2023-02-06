ip = list(map(int, input().split()))
lst = [4, 9, 25, 49, 121, 169]

for i in range(3, ip[1], 2):
    if (i**2) > ip[1]:
        break

    if (i % 5 == 0) or (i % 3 == 0) or (i % 7 == 0) or (i % 11 == 0) or (i % 13 == 0):
        continue

    lst.append(i**2)

nono = [True for _ in range(ip[0], ip[1]+1)]
for i in lst:
    for j in range(max(1, ip[0]//i), ip[1]):
        if i*j > ip[1]:
            break

        elif i*j >= ip[0]:
            nono[i * j - ip[0]] = False

cnt = nono.count(True)
print(cnt)
