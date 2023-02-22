lst = [0 for _ in range(43)]
cnt = 0
for i in range(10):
    n = int(input()) % 42
    if not lst[n]:
        lst[n] += 1
        cnt += 1
print(cnt)
