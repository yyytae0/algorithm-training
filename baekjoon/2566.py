lst = list()
for i in range(9):
    lst.append(list(map(int, input().split())))

target = 0
t_x = 1
t_y = 1
for i in range(1, 10):
    for j in range(1, 10):
        if lst[i-1][j-1] > target:
            target = lst[i-1][j-1]
            t_x = i
            t_y = j

print(target)
print(t_x, t_y)
