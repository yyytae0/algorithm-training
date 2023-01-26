def move(code, length, *x):
    if code == 1:
        x_new = [x[0]+length, x[1]]

    elif code == 2:
        x_new = [x[0]-length, x[1]]

    elif code == 3:
        x_new = [x[0], x[1]-length]

    elif code == 4:
        x_new = [x[0], x[1]+length]

    return x_new


n = int(input())
lst = list()
now = [0, 0]
x_lst = list()
y_lst = list()
for i in range(6):
    a, b = map(int, input().split())
    now = move(a, b, *now)
    if now[0] not in x_lst:
        x_lst.append(now[0])

    if now[1] not in y_lst:
        y_lst.append(now[1])

    lst.append(now)

x_lst.sort()
y_lst.sort()
x_new = [x_lst[0], x_lst[-1]]
y_new = [y_lst[0], y_lst[-1]]
ans = []
for i in x_new:
    for j in y_new:
        if [i, j] not in lst:
            ans = [i, j]
            break

    if len(ans) != 0:
        break

remain = abs((ans[0]-x_lst[1])*(ans[1]-y_lst[1]))
total = abs((x_new[0]-x_new[1])*(y_new[0]-y_new[1]))
print((total - remain)*n)
