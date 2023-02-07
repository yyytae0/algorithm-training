lst = list(map(int, input().split()))

ans = [1, 1, 1]
cnt = 1
while lst != ans:
    ans[0] += 1
    ans[1] += 1
    ans[2] += 1
    if ans[0] == 16:
        ans[0] = 1
    if ans[1] == 29:
        ans[1] = 1
    if ans[2] == 20:
        ans[2] = 1
    cnt += 1

print(cnt)
