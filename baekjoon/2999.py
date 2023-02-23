s = input()
n = len(s)
for i in range(int(n**(1/2)), 0, -1):
    if n % i == 0:
        r = i
        break

lst = [['' for _ in range(n//r)] for _ in range(r)]

idx = 0
for i in range(n//r):
    for j in range(r):
        lst[j][i] = s[idx]
        idx += 1

ans = ''
for i in range(r):
    for j in range(n//r):
        ans += lst[i][j]

print(ans)