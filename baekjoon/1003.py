ip = int(input())

for i in range(ip):
    num = int(input())

    if num == 0:
        print("%d %d" % (1, 0))

    else:
        a = 0
        b = 1
        for j in range(num - 1):
            dummy = a
            a = b
            b = dummy + b

        print("%d %d" % (a, b))
