a = input()
b = input()
na = len(a)
nb = len(b)
mx = [0, '']
dp = [[0, ''] for _ in range(nb)]
for i in a:
    d = [0, '']
    for j in range(nb):
        if dp[j][0] > d[0]:
            d = [dp[j][0], dp[j][1]]
        if i == b[j]:
            if d[0]+1 > dp[j][0]:
                dp[j] = [d[0]+1, d[1]+i]
        if dp[j][0] > mx[0]:
            mx = [dp[j][0], dp[j][1]]

dp = [[0, ''] for _ in range(na)]
for i in b:
    d = [0, '']
    for j in range(na):
        if dp[j][0] > d[0]:
            d = [dp[j][0], dp[j][1]]
        if i == a[j]:
            if d[0]+1 > dp[j][0]:
                dp[j] = [d[0]+1, d[1]+i]
        if dp[j][0] > mx[0]:
            mx = [dp[j][0], dp[j][1]]

print(mx[0])
print(mx[1])
