def check(n, target):
    total = n
    while n != 0:
        total = total + n%10
        n = n//10

    if total == target:
        return True

    else:
        return False


ip = int(input())
n_len = len(str(ip))
dummy = 0

if ip < 20:
    for i in range(1, ip):
        if check(i, ip):
            dummy = 1
            print(i)
            break

else:
    for i in range(ip - (9 * n_len), ip):
        if check(i, ip):
            dummy = 1
            print(i)
            break

if dummy == 0:
    print(0)
