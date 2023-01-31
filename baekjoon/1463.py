ip = int(input())
ans = [0] * (ip + 4)
ans[1] = 0
ans[2] = 1
ans[3] = 1
for i in range(4, ip+1):
    if i % 2 == 0 and i % 3 == 0:
        ans[i] = min(ans[i//3]+1, ans[i//2]+1, ans[i-1]+1)

    elif i % 2 == 0:
        ans[i] = min(ans[i//2]+1, ans[i-1]+1)

    elif i % 3 == 0:
        ans[i] = min(ans[i//3]+1, ans[i-1]+1)

    else:
        ans[i] = ans[i-1] + 1

print(ans[ip])
