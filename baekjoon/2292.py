n = int(input())
cnt = 6
now = 1
ans = 1
while n > now:
    ans += 1
    now += cnt
    cnt += 6
print(ans)
