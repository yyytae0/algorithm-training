ip = list(map(int, input().split()))
lst = [4]

for i in range(3, ip[1], 2):
    if (i**2) > ip[1]:
        break
    if i in lst:
        continue
    lst.append(i**2)

nono = [True]*(ip[1]+1)
nono[0] = False
print(lst)
for i in lst:
    for j in range(1, ip[1]):
        if i*j > ip[1]:
            break
        nono[i*j] = False

cnt = nono[ip[0]:ip[1]+1].count(True)
print(cnt)
