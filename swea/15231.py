ip = int(input())
anslst = list()

for i in range(1, ip+1):
    lst = list(map(int, input().split()))
    a = len(bin(lst[0])) - 3
    b = len(bin(lst[1])) - 3
    c = a + b
    if lst[1] == 1:
        c = a

    if lst[0] == 2:
        c = 1

    anslst.append("#%d %d" % (i, c))

result = "\n".join(anslst)
print(result)
