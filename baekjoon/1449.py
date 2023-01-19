ip = list(map(int, input().split()))
punk = list(map(int, input().split()))
punk.sort()
dummy = range(0)
cnt = 0

for i in range(ip[0]):
    if punk[i] in dummy:
        continue

    else:
        cnt += 1
        dummy = range(punk[i], punk[i]+ip[1])

print(cnt)
