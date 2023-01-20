def d(n):
    total = n
    while n != 0:
        total = total + n % 10
        n = n // 10

    return total


lst = [True] * 10001
lst[0] = False
s = ''

for i in range(1, 10001):
    if d(i) > 10000:
        if lst[i]:
            s = s + str(i) + '\n'
        continue

    else:
        lst[d(i)] = False

    if lst[i]:
        s = s + str(i) + '\n'

print(s)
