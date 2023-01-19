n = int(input())
cnt = 0
num2 = []
for i in range(20):
    num2.append(2**i)

while n != 1:
    if n % 3 == 0:
        n = n/3
        cnt += 1

    elif n in num2:
        n = n/2
        cnt += 1

    elif n % 3 == 1:
        n = n - 1
        cnt += 1

    else:
        n = n - 1
        cnt += 1

print(cnt)

