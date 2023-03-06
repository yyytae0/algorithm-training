n = int(input())
lst = list(map(int, input().split()))
ans1 = [0 for _ in range(n)]
ans2 = [0 for _ in range(n)]
lst.sort()
d = lst[:]
idx, step = n//2, 0
while lst:
    ans1[idx + step] = lst.pop()
    if lst:
        ans1[idx - 1 - step] = lst.pop(0)
    if step < 0:
        step = - 1 - step + 1
    else:
        step = - 1 - step - 1

idx, step = n//2, 0
while d:
    ans2[idx + step] = d.pop(0)
    if d:
        ans2[idx - 1 - step] = d.pop()
    if step < 0:
        step = - 1 - step + 1
    else:
        step = - 1 - step - 1

cnt1, cnt2 = 0, 0
for i in range(n-1):
    cnt1 += abs(ans1[i]-ans1[i+1])
    cnt2 += abs(ans2[i]-ans2[i+1])
cnt = max(cnt1, cnt2)
print(cnt)
