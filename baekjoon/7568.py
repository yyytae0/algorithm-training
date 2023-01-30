ip = int(input())
lst = list()
for i in range(ip):
    lst.append(list(map(int, input().split())))

rank = list()
for i in range(ip):
    cnt = 0
    for j in range(ip):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    rank.append(cnt+1)

print(*rank)
