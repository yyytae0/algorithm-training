from sys import stdin

n = int(stdin.readline())
sx, sy = map(int, stdin.readline().split())
dx, dy = sx, sy
ans = 0
for i in range(n-1):
    a, b = map(int, stdin.readline().split())
    ans += dx*b - dy*a
    dx, dy = a, b
ans += dx*sy - dy*sx
ans = abs(ans) * 1/2
print(ans)
