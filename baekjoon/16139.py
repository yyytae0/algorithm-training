from sys import stdin, stdout

ip = stdin.readline().strip()
nip = len(ip)
n = int(stdin.readline())
dp = [[0 for _ in range(nip)] for _ in range(26)]
for i in range(nip):
    for j in range(i, nip):
        dp[ord(ip[i]) - 97][j] += 1

for _ in range(n):
    a, i, j = stdin.readline().split()
    i, j = int(i), int(j)
    if i > 0:
        ans = dp[ord(a)-97][j] - dp[ord(a)-97][i-1]
    else:
        ans = dp[ord(a)-97][j]
    stdout.write(str(ans) + '\n')
