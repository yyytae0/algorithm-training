ip = input().split()

a = len(ip[0])
b = len(ip[1])
ans = 100

if a == b:
    cnt = 0
    for i in range(a):
        if ip[0][i] != ip[1][i]:
            cnt += 1
    ans = cnt

else:
    for i in range(b-a + 1):
        cnt = 0
        for j in range(a):
            if ip[0][j] != ip[1][j+i]:
                cnt += 1

        if cnt < ans:
            ans = cnt

print(ans)
