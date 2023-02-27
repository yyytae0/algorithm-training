def change():
    new = ['' for _ in range(n)]
    a = 1
    for i in range(n):
        new[rule[i]] = now[i]
        if ans[rule[i]] != now[i]:
            a = 0
    return a, new


n = int(input())
now = list(input().split())
rule = list(map(int, input().split()))
dummy = [now]
ans = ['0', '1', '2'] * (n//3)
cnt = 0
if now == ans:
    print(0)
else:
    a = 0
    while not a:
        a, now = change()
        cnt += 1
        if now in dummy:
            cnt = -1
            break
        dummy.append(now)
    print(cnt)
