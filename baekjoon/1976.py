def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


def check():
    for i in range(m-1):
        if d[t[i]-1][t[i+1]-1] == float('inf'):
            return 'NO'
    return 'YES'


n = int(input())
m = int(input())
d = list(list(map(int, input().split())) for _ in range(n))
for i in range(n):
    for j in range(n):
        if i != j and d[i][j] == 0:
            d[i][j] = float('inf')
floyd_warshall()
t = list(map(int, input().split()))
print(check())
ㄴ