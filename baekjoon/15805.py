n = int(input())
lst = list(map(int, input().split()))
visit = [-2 for _ in range(n)]
dummy = -1
for i in lst:
    if visit[i] == -2:
        visit[i] = dummy
    dummy = i

cnt = 0
for i in visit:
    if i > -2:
        cnt += 1
    else:
        break
print(cnt)
print(*visit[:cnt])