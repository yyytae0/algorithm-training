from sys import stdin


n = int(stdin.readline())
lst = list(list(map(int, stdin.readline().split())) for _ in range(n))
mx1, mx2, mx3 = lst[0][0], lst[0][1], lst[0][2]
mn1, mn2, mn3 = lst[0][0], lst[0][1], lst[0][2]
for i in range(1, n):
    mx1, mx2, mx3 = max(mx1, mx2) + lst[i][0], max(mx1, mx2, mx3) + lst[i][1], max(mx3, mx2) + lst[i][2]
    mn1, mn2, mn3 = min(mn1, mn2) + lst[i][0], min(mn1, mn2, mn3) + lst[i][1], min(mn3, mn2) + lst[i][2]

print(max(mx1, mx2, mx3), min(mn1, mn2, mn3))
