def calc(a, b, c, d):
    return ((a-c)**2 + (b-d)**2)**(1/2)


n = int(input())
dist = [[float("inf") for _ in range(n)] for _ in range(n)]
lst = [list(map(float, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        d = calc(lst[i][0], lst[i][1], lst[j][0], lst[j][1])
        dist[i][j], dist[j][i] = d, d

print(dist)
