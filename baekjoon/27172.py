n = int(input())
lst = list(map(int, input().split()))
MX = max(lst)
cnt = [0 for _ in range(MX+1)]
ans = [0 for _ in range(MX+1)]
for i in lst:
    cnt[i] = 1

for i in range(MX+1):
    if cnt[i]:
        for j in range(2, MX+1):
            if i*j > MX:
                break
            if cnt[i*j]:
                ans[i] += 1
                ans[i*j] -= 1

for i in lst:
    print(ans[i], end=" ")
