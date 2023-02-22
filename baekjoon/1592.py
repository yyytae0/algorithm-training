n, m, l = map(int, input().split())
lst = [0 for _ in range(n)]
lst[0] = 1
now = 0
cnt = 0
while lst[now] < m:
    cnt += 1
    if lst[now] % 2:
        now = (now + l) % n
        lst[now] += 1
    else:
        now = now - l if now - l >= 0 else n + now - l
        lst[now] += 1
print(cnt)
