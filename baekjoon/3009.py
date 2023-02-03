lst = list(list(map(int, input().split())) for _ in range(3))
ansx = list()
ansy = list()
for i in lst:
    if i[0] in ansx:
        ansx.remove(i[0])

    else:
        ansx.append(i[0])

    if i[1] in ansy:
        ansy.remove(i[1])

    else:
        ansy.append(i[1])

print(ansx[0], ansy[0])
