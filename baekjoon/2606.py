ip = int(input())
n = int(input())
lst = list()

for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort()

a = {1}

for i in range(1, ip+1):
    for j in lst:
        if i in j:
            if (j[0] in a) or (j[1] in a):
                a.add(j[0])
                a.add(j[1])

print(len(a)-1)
