ip = input()
dummy = ''
cnt = 0

for i in ip:
    if dummy == i:
        continue

    else:
        cnt += 1
        dummy = i

print(cnt//2)
