lst = list(list(map(int, input().split())) for _ in range(4))

ans = [[0 for _ in range(100)] for _ in range(100)]

for i in lst:
    for j in range(i[0], i[2]):
        for k in range(i[1], i[3]):
            ans[j][k] = 1

total = 0
for i in ans:
    total = total + i.count(1)

print(total)
