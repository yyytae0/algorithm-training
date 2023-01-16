ip = int(input())

lst = list(map(int, input().split()))
ans = [0 for j in range(ip)]
cnt = 0
for i in range(1, 1001):
    if i in lst:
        for j in range(ip):
            if lst[j] == i:
                ans[j] = cnt
                cnt += 1

print(*ans)
