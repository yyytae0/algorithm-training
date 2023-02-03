ip = int(input())
lst = list()
ans = [[0 for _ in range(100)] for _ in range(100)]

for i in range(ip):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            ans[j][k] = 1

cnt = 0
for i in ans:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)
