n, k = map(int, input().split())
num = dict()
for j in range(n):
    s, y = map(int, input().split())
    if (s, y) in num.keys():
        num[(s, y)] += 1

    else:
        num[(s, y)] = 1

cnt = 0
for j in num.values():
    cnt += 1
    while j > k:
        j = j-k
        cnt += 1

print(cnt)
