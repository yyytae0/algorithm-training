l = int(input())
n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
bread = [0 for _ in range(l)]
idx = 1
ans1 = [0, 0]
ans2 = [0, 0]
for i in lst:
    if i[1] - i[0] > ans1[0]:
        ans1 = [i[1]-i[0], idx]
    for j in range(i[0]-1, i[1]):
        if not bread[j]:
            bread[j] = idx
    idx += 1

for i in range(1, n+1):
    d = bread.count(i)
    if d > ans2[0]:
        ans2 = [d, i]

print(ans1[1])
print(ans2[1])
