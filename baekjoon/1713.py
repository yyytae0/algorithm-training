n = int(input())
m = int(input())
lst = list(map(int, input().split()))
photo = []
cnt = 0
for i in lst:
    for idx, j in enumerate(photo):
        if i == j[2]:
            photo[idx][0] += 1
            break
    else:
        if len(photo) == n:
            photo.pop()
        photo.append([1, cnt, i])
        cnt += 1
    photo.sort(key=lambda x: (-x[0], -x[1]))
ans = []
for i in photo:
    ans.append(i[2])
ans.sort()
print(*ans)
