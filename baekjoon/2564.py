x, y = map(int, input().split())
n = int(input())
lst = list()

for i in range(n):
    code, far = map(int, input().split())
    lst.append([code, far])

code, far = map(int, input().split())
total = 0

if code == 1:
    for i in lst:
        if i[0] == 3:
            total = total + i[1] + far

        elif i[0] == 4:
            total = total + (x-far) + i[1]

        elif i[0] == 1:
            total = total + abs(i[1]-far)

        elif i[0] == 2:
            a = i[1] + far + y
            b = x*2 - i[1] - far + y
            total = total + min(a, b)

elif code == 2:
    for i in lst:
        if i[0] == 3:
            total = total + y - i[1] + far

        elif i[0] == 4:
            total = total + (x-far) + y - i[1]

        elif i[0] == 2:
            total = total + abs(i[1]-far)

        elif i[0] == 1:
            a = i[1] + far + y
            b = x*2 - i[1] - far + y
            total = total + min(a, b)

elif code == 3:
    for i in lst:
        if i[0] == 1:
            total = total + i[1] + far

        elif i[0] == 2:
            total = total + (y-far) + i[1]

        elif i[0] == 3:
            total = total + abs(i[1]-far)

        elif i[0] == 4:
            a = i[1] + far + x
            b = y*2 - i[1] - far + x
            total = total + min(a, b)

elif code == 4:
    for i in lst:
        if i[0] == 1:
            total = total + x - i[1] + far

        elif i[0] == 2:
            total = total + (y-far) + x - i[1]

        elif i[0] == 4:
            total = total + abs(i[1]-far)

        elif i[0] == 3:
            a = i[1] + far + x
            b = y*2 - i[1] - far + x
            total = total + min(a, b)

print(total)
