n = int(input())
lst = list(map(int, input().split()))
t = int(input())
q = list()
q.append(t)
lst[t] = -2
while q:
    v = q.pop(0)
    for i in range(n):
        if lst[i] == v:
            q.append(i)
            lst[i] = -2
ans = [0 for _ in range(n)]
for i in range(n):
    if lst[i] != -2:
        ans[i] = 1
for i in range(n):
    if lst[i] >= 0:
        ans[lst[i]] = 0
print(sum(ans))
