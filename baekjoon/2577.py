sm = 1

for i in range(3):
    a = int(input())
    sm = sm * a

cnt = {}

for i in range(10):
    cnt[i] = 0

while True:
    a = sm % 10
    cnt[a] += 1
    sm = sm // 10
    if sm < 10:
        cnt[sm] += 1
        break

for i in range(10):
    print(cnt[i])
