ip = int(input())
lst = list()
for i in range(ip):
    n = int(input())
    if n == 0:
        lst.pop()

    else:
        lst.append(n)

print(sum(lst))
